#tblview.clicked.connect(ibswgt.on_click)

#def _init_redirects(ibswgt):
#    """
#    redirects allows user to go from a row of a table to corresponding rows
#    of other tables
#    """
#    redirects = gh.get_redirects(ibswgt.ibs)
#    for src_table in redirects.keys():
#        for src_table_name in redirects[src_table].keys():
#            dst_table, mapping_func = redirects[src_table][src_table_name]
#            src_table_col = gh.TABLE_COLNAMES[src_table].index(src_table_name)
#            ibswgt.register_redirect(src_table, src_table_col, dst_table, mapping_func)

@slot_(QtCore.QModelIndex)
def on_click(ibswgt, qtindex):
    """
    Clicking anywhere in the GUI

    DOENT DO ANYTHING ANYMORE SELECTION MODEL USED INSTEAD

    DEPRICATE
    """
    return
    #printDBG('on_click')
    model = qtindex.model()
    id_ = model._get_row_id(qtindex)
    #model_name = model.name
    #print('clicked: %s' + ut.dict_str(locals()))
    if False:
        try:
            dst_table, mapping_func = ibswgt.redirects[model.name][qtindex.column()]
            dst_id = mapping_func(id_)
            print("[on_click] Redirecting to: %r" % (dst_table, ))
            print("[on_click]     Mapping %r -> %r" % (id_, dst_id, ))
            ibswgt.set_table_tab(dst_table)
            ibswgt.views[dst_table].select_row_from_id(id_, scroll=True)
            return None
        except Exception as ex:
            print('no redirects')
            if ut.VERYVERBOSE:
                ut.printex(ex, 'no redirect listed for this table', iswarning=True)
            # No redirect listed for this table
            pass

    # If no link, process normally
    if model.name == IMAGESET_TABLE:
        pass
        #printDBG('clicked imageset')
    else:
        table_key = model.name
        # FIXME: stripe model needs to forward get_level
        if not hasattr(model, '_get_level'):
            level = 0
        else:
            level = model._get_level(qtindex)
        imgsetid = model.imgsetid
        ibswgt.select_table_id(table_key, level, id_, imgsetid)

            #model._update_rows()

        #model = ibswgt.models[gh.NAMES_TREE]  # NOQA
        ##model.set_ider_filters([ut.identity, filter_fn])
        #model.set_ider_filters([ut.identity, lambda aids_list: [filter_fn(aids) for aids in aids_list]])
        #with ChangeLayoutContext([model]):
        #    model._update_rows(rebuild_structure=True)

        #def get_error_aids():
        #    # DISABLE_DOCTEST
        #    aid_list = ibs.get_valid_aids()
        #    #filter_kw = dict(is_known=True, min_num=1, has_any='viewpoint')
        #    aid_list_ = ibs.filter_annots_general(aid_list, filter_kw)

        #def get_aids_with_annotmatchprop():
        #    from ibeis import constants as const
        #    from ibeis.control import _autogen_annotmatch_funcs
        #    colnames = (_autogen_annotmatch_funcs.ANNOT_ROWID1,
        #    _autogen_annotmatch_funcs.ANNOT_ROWID2)
        #    tblname = const.ANNOTMATCH_TABLE
        #    wherecol = _autogen_annotmatch_funcs.ANNOTMATCH_IS_SCENERYMATCH
        #    whereclause = wherecol + '=?'
        #    colname_str = ', '.join(colnames)
        #    operation = ut.codeblock(
        #        '''
        #        SELECT {colname_str}
        #        FROM {tblname}
        #        WHERE {whereclause}
        #        ''').format(colname_str=colname_str, tblname=tblname, whereclause=whereclause)

        #    ibs.db.cur.execute(operation, [True])
        #    scenery_aids = list(set(ut.flatten(ibs.db.cur.fetchall())))
        #    return scenery_aids

        #annotmatch_rowid_list = ibs._get_all_annotmatch_rowids()
        #ishard_list         = ibs.get_annotmatch_is_hard(annotmatch_rowid_list)
        #isphotobomb_list    = ibs.get_annotmatch_is_photobomb(annotmatch_rowid_list)
        #isscenerymatch_list = ibs.get_annotmatch_is_scenerymatch(annotmatch_rowid_list)
        #isnondistinct_list  = ibs.get_annotmatch_is_nondistinct(annotmatch_rowid_list)
        #hards        = np.array(ut.replace_nones(ishard_list, False))
        #photobombs   = np.array(ut.replace_nones(isphotobomb_list, False))
        #scenerys     = np.array(ut.replace_nones(isscenerymatch_list, False))
        #nondistincts = np.array(ut.replace_nones(isnondistinct_list, False))
        #flags = vt.and_lists(vt.or_lists(hards, nondistincts), ~photobombs, ~scenerys)
        #annotmatch_rowid_list_ = ut.compress(annotmatch_rowid_list, flags)

        #aid1_list = ibs.get_annotmatch_aid1(annotmatch_rowid_list_)
        #aid2_list = ibs.get_annotmatch_aid2(annotmatch_rowid_list_)
        #aid_list = sorted(list(set(aid1_list + aid2_list)))

        #def filter_to_background(aid_list, ibs=ibswgt.back.ibs):
        #    ibswgt.back.ibs
        #pass


                #[
                #    ('Go to image',
                #     lambda: ibswgt.goto_table_id(IMAGE_TABLE,
                #                                  ibswgt.back.ibs.get_annot_gids(aid))),
                #    ('Go to annotation',
                #     lambda: ibswgt.goto_table_id(gh.ANNOTATION_TABLE, aid)),
                #    ('----', lambda: None),
                #    ('View annotation in Matplotlib',
                #     lambda: ibswgt.back.select_aid(aid, imgsetid, show=False)),
                #    ('View annotation in Web',
                #     lambda: ibswgt.back.select_aid(aid, imgsetid, show=True)),
                #    ('View image in Matplotlib',
                #     lambda: ibswgt.back.select_gid_from_aid(aid, imgsetid, show=True, web=False)),
                #    ('View image in Web',
                #     lambda: ibswgt.back.select_gid_from_aid(aid, imgsetid, show=True, web=True)),
                #]


                    #('View annotation in Matplotlib',
                    #    #lambda: ibswgt.back.select_aid(aid, imgsetid, show=True)),
                    #    lambda: ibswgt.back.show_annotation(aid, web=False)),
                    #('View image in Matplotlib',
                    #    lambda: ibswgt.back.select_gid_from_aid(aid, imgsetid, show=True, web=False)),
                    #('View detection chip (probability) [dev]',
                    #    lambda: ibswgt.back.show_probability_chip(aid)),



def get_training_desc_dist_OLD(cm, qreq_, fsv_col_lbls, namemode=True):
    """
    computes custom distances on prematched descriptors

    CommandLine:
        python -m ibeis.algo.hots.chip_match --exec-get_training_desc_dist --show

    Example:
        >>> # ENABLE_DOCTEST
        >>> from ibeis.algo.hots.chip_match import *  # NOQA
        >>> cm, qreq_ = testdata_cm()
        >>> fsv_col_lbls = ['L2_sift']
        >>> (tp_fsv, tn_fsv) = get_training_desc_dist(cm, qreq_, fsv_col_lbls,
        >>>                                           namemode=False)
        >>> result = ut.repr2((tp_fsv, tn_fsv), nl=1)
        >>> print(result)

    Example:
        >>> # ENABLE_DOCTEST
        >>> from ibeis.algo.hots.chip_match import *  # NOQA
        >>> cm, qreq_ = testdata_cm()
        >>> #cm, qreq_ = ibeis.testdata_cm(a=['default:dsize=20,qindex=0:1,pername=1'])
        >>> fsv_col_lbls = ['ratio']
        >>> namemode = False
        >>> (tp_fsv, tn_fsv) = get_training_desc_dist(cm, qreq_, fsv_col_lbls,
        >>>                                           namemode=False)
        >>> result = ut.repr2((tp_fsv, tn_fsv), nl=1)
        >>> print(result)
    """
    ibs = qreq_.ibs
    qaid = cm.qaid
    if namemode:
        tp_idxs, tn_idxs = get_topname_training_idxs(cm)
    else:
        tp_idxs, tn_idxs = get_topannot_training_idxs(cm)
    tp_daids = cm.daid_list.take(tp_idxs)
    tn_daids = cm.daid_list.take(tn_idxs)
    tp_fm = ut.list_take(cm.fm_list, tp_idxs)
    tn_fm = ut.list_take(cm.fm_list, tn_idxs)
    tp_fx0 = [fm.T[0] for fm in tp_fm]
    tn_fx0 = [fm.T[0] for fm in tn_fm]
    tp_fx1 = [fm.T[1] for fm in tp_fm]
    tn_fx1 = [fm.T[1] for fm in tn_fm]
    query_config2_ = qreq_.extern_query_config2
    data_config2_ = qreq_.extern_data_config2
    special_xs, dist_xs = vt.index_partition(fsv_col_lbls, ['fg'])
    dist_lbls = ut.list_take(fsv_col_lbls, dist_xs)
    special_lbls = ut.list_take(fsv_col_lbls, special_xs)

    if len(special_xs) > 0:
        assert special_lbls[0] == 'fg'
        # hack for fgweights (could get them directly from fsv)
        qfgweights = ibs.get_annot_fgweights([qaid],
                                             config2_=query_config2_)[0]
        tp_dfgweights = ibs.get_annot_fgweights(tp_daids,
                                                config2_=data_config2_)
        tn_dfgweights = ibs.get_annot_fgweights(tn_daids,
                                                config2_=data_config2_)
        # Align weights
        tp_qfgweights_m = vt.ziptake([qfgweights] * len(tp_fx0),
                                     tp_fx0, axis=0)
        tn_qfgweights_m = vt.ziptake([qfgweights] * len(tn_fx0),
                                     tn_fx0, axis=0)
        tp_dfgweights_m = vt.ziptake(tp_dfgweights, tp_fx1, axis=0)
        tn_dfgweights_m = vt.ziptake(tn_dfgweights, tn_fx1, axis=0)
        tp_qfgweights_flat_m = np.hstack(tp_qfgweights_m)
        tn_qfgweights_flat_m = np.hstack(tn_qfgweights_m)
        tp_dfgweights_flat_m = np.hstack(tp_dfgweights_m)
        tn_dfgweights_flat_m = np.hstack(tn_dfgweights_m)
        tp_fgweights = np.sqrt(tp_qfgweights_flat_m *
                               tp_dfgweights_flat_m)
        tn_fgweights = np.sqrt(tn_qfgweights_flat_m *
                               tn_dfgweights_flat_m)
        special_tp_dists = tp_fgweights[:, None]
        special_tn_dists = tn_fgweights[:, None]
    else:
        special_tp_dists = np.empty((0, 0))
        special_tn_dists = np.empty((0, 0))
    if len(dist_xs) > 0:
        # Get descriptors
        qvecs = ibs.get_annot_vecs(qaid, config2_=query_config2_)
        tp_dvecs = ibs.get_annot_vecs(tp_daids, config2_=data_config2_)
        tn_dvecs = ibs.get_annot_vecs(tn_daids, config2_=data_config2_)
        # Align descriptors
        tp_qvecs_m = vt.ziptake([qvecs] * len(tp_fx0), tp_fx0, axis=0)
        tn_qvecs_m = vt.ziptake([qvecs] * len(tn_fx0), tn_fx0, axis=0)
        tp_dvecs_m = vt.ziptake(tp_dvecs, tp_fx1, axis=0)
        tn_dvecs_m = vt.ziptake(tn_dvecs, tn_fx1, axis=0)
        tp_qvecs_flat_m = np.vstack(tp_qvecs_m)
        tn_qvecs_flat_m = np.vstack(tn_qvecs_m)
        tp_dvecs_flat_m = np.vstack(tp_dvecs_m)
        tn_dvecs_flat_m = np.vstack(tn_dvecs_m)
        # Compute descriptor distnaces
        _tp_dists = vt.compute_distances(
            tp_qvecs_flat_m, tp_dvecs_flat_m, dist_lbls)
        _tn_dists = vt.compute_distances(
            tn_dvecs_flat_m, tn_qvecs_flat_m, dist_lbls)
        tp_dists = np.vstack(_tp_dists.values()).T
        tn_dists = np.vstack(_tn_dists.values()).T
    else:
        tp_dists = np.empty((0, 0))
        tn_dists = np.empty((0, 0))

    tp_fsv = vt.rebuild_partition(special_tp_dists.T, tp_dists.T,
                                  special_xs, dist_xs)
    tn_fsv = vt.rebuild_partition(special_tn_dists.T, tn_dists.T,
                                  special_xs, dist_xs)
    tp_fsv = np.array(tp_fsv).T
    tn_fsv = np.array(tn_fsv).T
    return tp_fsv, tn_fsv


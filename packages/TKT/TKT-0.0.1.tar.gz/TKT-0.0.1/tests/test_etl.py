# coding: utf-8
# 2019/12/11 @ tongshiwei


from longling.lib.structure import AttrDict
from TKT import extract, pseudo_data_generation


def test_extract(train_dataset, test_dataset):
    for _ in extract(train_dataset):
        pass
    else:
        assert True
    for _ in extract(test_dataset):
        pass
    else:
        assert True


def test_pseudo():
    pseudo_data_generation(AttrDict({"hyper_params": {"ku_num": 10}}))

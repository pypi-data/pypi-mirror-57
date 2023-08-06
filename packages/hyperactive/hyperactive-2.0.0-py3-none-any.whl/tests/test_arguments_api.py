# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from hyperactive import Hyperactive

data = load_iris()
X = data.data
y = data.target


def model(para, X, y):
    model = DecisionTreeClassifier(
        max_depth=para["max_depth"],
        min_samples_split=para["min_samples_split"],
        min_samples_leaf=para["min_samples_leaf"],
    )
    scores = cross_val_score(model, X, y, cv=3)

    return scores.mean()


search_config = {
    model: {
        "max_depth": range(1, 21),
        "min_samples_split": range(2, 21),
        "min_samples_leaf": range(1, 21),
    }
}


def test_func_return():
    def model1(para, X, y):
        model = DecisionTreeClassifier(
            criterion=para["criterion"],
            max_depth=para["max_depth"],
            min_samples_split=para["min_samples_split"],
            min_samples_leaf=para["min_samples_leaf"],
        )
        scores = cross_val_score(model, X, y, cv=3)

        return scores.mean(), model

    search_config1 = {
        model1: {
            "criterion": ["gini", "entropy"],
            "max_depth": range(1, 21),
            "min_samples_split": range(2, 21),
            "min_samples_leaf": range(1, 21),
        }
    }

    opt = Hyperactive(X, y)
    opt.search(search_config1)


def test_n_jobs_2():
    opt = Hyperactive(X, y)
    opt.search(search_config, n_jobs=2)


def test_n_jobs_4():
    opt = Hyperactive(X, y)
    opt.search(search_config, n_jobs=4)


def test_positional_args():
    opt0 = Hyperactive(X, y, random_state=False)
    opt0.search(search_config)

    opt1 = Hyperactive(X, y, random_state=1)
    opt1.search(search_config)

    opt2 = Hyperactive(X, y, random_state=1)
    opt2.search(search_config)


def test_random_state():
    opt0 = Hyperactive(X, y, random_state=False)
    opt0.search(search_config)

    opt1 = Hyperactive(X, y, random_state=0)
    opt1.search(search_config)

    opt2 = Hyperactive(X, y, random_state=1)
    opt2.search(search_config)


def test_max_time():
    opt0 = Hyperactive(X, y)
    opt0.search(search_config, max_time=0.00001)


def test_memory():
    opt0 = Hyperactive(X, y, memory=True)
    opt0.search(search_config)

    opt1 = Hyperactive(X, y, memory=False)
    opt1.search(search_config)

    opt2 = Hyperactive(X, y, memory="short")
    opt2.search(search_config)

    opt3 = Hyperactive(X, y, memory="long")
    opt3.search(search_config)


def test_verbosity():
    opt0 = Hyperactive(X, y, verbosity=0)
    opt0.search(search_config)

    opt0 = Hyperactive(X, y, verbosity=0)
    opt0.search(search_config, n_jobs=2)

    opt1 = Hyperactive(X, y, verbosity=1)
    opt1.search(search_config)

    opt0 = Hyperactive(X, y, verbosity=1)
    opt0.search(search_config)

    opt1 = Hyperactive(X, y, verbosity=2)
    opt1.search(search_config)

    opt1 = Hyperactive(X, y, verbosity=2)
    opt1.search(search_config, n_jobs=2)


def test_scatter_init():
    init_config = {model: {"scatter_init": 10}}
    opt = Hyperactive(X, y)
    opt.search(search_config, init_config=init_config)


def test_warm_start():
    init_config = {
        model: {"max_depth": 10, "min_samples_split": 2, "min_samples_leaf": 5}
    }
    opt = Hyperactive(X, y, memory=False)
    opt.search(search_config, n_iter=0, init_config=init_config)

    assert opt.results_params[model] == init_config[model]


def test_partial_warm_start():
    init_config = {model: {"min_samples_split": 2, "min_samples_leaf": 5}}
    opt = Hyperactive(X, y, memory=False)
    opt.search(search_config, n_iter=0, init_config=init_config)


def test_optimizer_args():
    opt = Hyperactive(X, y)
    opt.search(search_config, optimizer={"HillClimbing": {"epsilon": 0.1}})


def test_get_search_path():
    opt = Hyperactive(X, y, verbosity=10)
    opt.search(search_config)

    opt = Hyperactive(X, y, verbosity=10)
    opt.search(search_config, optimizer="ParticleSwarm")


def test_ray_1():
    import ray

    ray.init()
    opt = Hyperactive(X, y)
    opt.search(search_config, n_jobs=1)


def test_ray_2():
    import ray

    ray.init()
    opt = Hyperactive(X, y)
    opt.search(search_config, n_jobs=2)

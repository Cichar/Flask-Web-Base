# encoding:utf-8

from flask import request, render_template


def pjax(template, **kwargs):
    """ PJAX """

    if "X-PJAX" in request.headers:
        return render_template(template, **kwargs)
    return render_template("base.html", template=template, **kwargs)

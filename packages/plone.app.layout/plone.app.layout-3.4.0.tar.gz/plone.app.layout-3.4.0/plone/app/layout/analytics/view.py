# -*- coding: utf-8 -*-
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import ISiteSchema
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.interface import implementer
from zope.viewlet.interfaces import IViewlet


@implementer(IViewlet)
class AnalyticsViewlet(BrowserView):

    render = ViewPageTemplateFile('view.pt')

    def __init__(self, context, request, view, manager):
        super(AnalyticsViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.webstats_js = ''

    def update(self):
        """render the webstats snippet"""
        registry = getUtility(IRegistry)
        site_settings = registry.forInterface(
            ISiteSchema, prefix="plone", check=False)
        try:
            if site_settings.webstats_js:
                self.webstats_js = site_settings.webstats_js
        except AttributeError:
            pass

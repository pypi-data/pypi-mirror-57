from functools import partial

from pyramid.view import view_config, view_defaults
from sqlalchemy.orm import subqueryload

from c2cgeoform.schema import GeoFormSchemaNode
from c2cgeoform.views.abstract_views import ListField

from getitfixed.models.getitfixed import (
    Event,
    Category,
    Issue,
    Type,
    USER_ADMIN,
    STATUS_IN_PROGRESS,
    STATUS_VALIDATED,
    STATUS_REPORTER,
    STATUS_NEW,
)
from getitfixed.views.private.semi_private_issues import IssueViews

_list_field = partial(ListField, Issue)

base_schema = GeoFormSchemaNode(Issue, excludes=["events", "public_events"])
route = "c2cgeoform_item"
event_schema = GeoFormSchemaNode(Event)


@view_defaults(
    match_param=("application=getitfixed_admin", "table=issues"),
    permission="getitfixed_admin",
)
class IssueAdminViews(IssueViews):

    _author = USER_ADMIN
    _event_schema = event_schema
    _application = "getitfixed_admin"

    _list_fields = [
        _list_field("id"),
        _list_field("status"),
        _list_field("request_date"),
        _list_field(
            "type_id",
            renderer=lambda issue: issue.type.label_fr,
            sort_column=Type.label_fr,
            filter_column=Type.label_fr,
        ),
        _list_field("description"),
        _list_field("localisation"),
        _list_field("firstname"),
        _list_field("lastname"),
        _list_field("phone"),
        _list_field("email"),
    ]
    _list_ordered_fields = [Issue.request_date.desc()]

    def _base_query(self):
        query = (
            super()
            ._base_query()
            .outerjoin(Issue.type)
            .options(subqueryload(Issue.type))
        )
        # return all issues that are not closed
        if self._request.params.get("all") != "true":
            query = query.filter(
                Issue.status.in_(
                    [STATUS_IN_PROGRESS, STATUS_VALIDATED, STATUS_REPORTER, STATUS_NEW]
                )
            )
        category_filter = int(self._request.params.get("category", 0))

        # filter issues based on category id
        if category_filter != 0:  # 0 is for all issues
            query = query.filter(Issue.category.has(id=category_filter))
        return query

    @view_config(
        route_name="c2cgeoform_index",
        renderer="getitfixed:templates/admin/issues/index.jinja2",
    )
    def index(self):
        resp = super().index()
        cats = self._request.dbsession.query(Category).all()

        label = (
            "label_fr" if self._request.localizer.locale_name == "fr" else "label_en"
        )
        resp.update(
            {
                "categories": list(
                    map(lambda c: {"id": c.id, "value": getattr(c, label)}, cats)
                )
            }
        )
        return resp

    @view_config(route_name="c2cgeoform_grid", renderer="json")
    def grid(self):
        return super().grid()

    def _grid_actions(self):
        return []

    def _item_actions(self, item):
        return []

    @view_config(
        route_name="c2cgeoform_item",
        request_method="GET",
        renderer="getitfixed:templates/admin/issues/edit.jinja2",
    )
    def edit(self):
        return super().edit()

    @staticmethod
    def events(issue):
        return issue.events

    @view_config(
        route_name="c2cgeoform_item",
        request_method="POST",
        renderer="getitfixed:templates/admin/issues/edit.jinja2",
    )
    def save(self):
        return super().save()

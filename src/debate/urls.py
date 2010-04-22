from django.conf.urls.defaults import *

from django.core.urlresolvers import reverse

urlpatterns = patterns('debate.views',
    url(r'^$', 'index', name='debate_index'),
    url(r'^draw/$', 'draw_index', name='draw_index'),
    url(r'^round/(?P<round_id>\d+)/$',
        'round_index', name='round_index'),
    url(r'^round/(?P<round_id>\d+)/venues/$',
        'venue_availability', name='venue_availability'),
    url(r'^round/(?P<round_id>\d+)/venues/update/$',
        'update_venue_availability', name='update_venue_availability'),
    url(r'^round/(?P<round_id>\d+)/adjudicators/$',
        'adjudicator_availability', name='adjudicator_availability'),
    url(r'^round/(?P<round_id>\d+)/adjudicators/update/$',
        'update_adjudicator_availability', name='update_adjudicator_availability'),
    url(r'^round/(?P<round_id>\d+)/teams/$',
        'team_availability', name='team_availability'),
    url(r'^round/(?P<round_id>\d+)/teams/update/$',
        'update_team_availability', name='update_team_availability'),
    url(r'^round/(?P<round_id>\d+)/draw/$', 'draw',
        name='draw'),
    url(r'^round/(?P<round_id>\d+)/draw/create/$', 'create_draw',
        name='create_draw'),
    url(r'^round/(?P<round_id>\d+)/draw/confirm/$', 'confirm_draw',
        name='confirm_draw'),

    url(r'^round/(?P<round_id>\d+)/draw/venues/$', 'draw_venues_edit',
        name='draw_venues_edit'),
    url(r'^round/(?P<round_id>\d+)/draw/venues/save/$', 'save_venues',
        name='save_venues'),

    url(r'^round/(?P<round_id>\d+)/draw/adjudicators/$', 'draw_adjudicators_edit',
        name='draw_adjudicators_edit'),
    url(r'^round/(?P<round_id>\d+)/draw/adjudicators/save/$', 'save_adjudicators',
        name='save_adjudicators'),

    url(r'^round/(?P<round_id>\d+)/adj_allocation/create/$',
        'create_adj_allocation',
        name='create_adj_allocation'),
    url(r'^round/(?P<round_id>\d+)/results/$', 'results',
        name='results'),
    url(r'^round/(?P<round_id>\d+)/team_standings/$', 'team_standings',
        name='team_standings'),
    url(r'^debate/(?P<debate_id>\d+)/results/$', 'enter_result',
        name='enter_result'),
    url(r'^debate/(?P<debate_id>\d+)/results/save/$', 'save_result',
        name='save_result'),

    url(r'^round/(?P<round_id>\d+)/adjudicators/conflicts/$', 'adj_conflicts', name='adj_conflicts'),
    url(r'^adjudicators/scores/$', 'adj_scores', name='adj_scores'),
    url(r'^adjudicators/feedback/$', 'adj_feedback', name='adj_feedback'),
    url(r'^adjudicators/feedback/get/$', 'get_adj_feedback', name='get_adj_feedback'),
    url(r'^adjudicators/feedback/(?P<adjudicator_id>\d+)/$', 
        'enter_feedback', name='enter_feedback'),
    )



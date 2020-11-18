"""oddstracker_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from oddstracker import views
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

router = SimpleRouter()
router.include_format_suffixes = False
router.register(r'games', views.GameViewSet)

gameodds_detail = views.GameOddsViewSet.as_view({
    'get': 'retrieve'
})

gameodds_list = views.GameOddsViewSet.as_view({
    'post': 'create'
})

games_list = views.GameViewSet.as_view({
    'get': 'list'
})



urlpatterns = [
    path('api/games/<int:pk>/odds/', gameodds_detail, name="gameodds-detail"),
    path('api/game-odds/', gameodds_list, name="gameodds-list"),
    path('api/', include(router.urls)),
    path('api/games/', games_list, name="game-list")

    # path('admin/', admin.site.urls),
    # re_path(r'^api/games/$', views.GameViewSet, name="games-list"),
    # path('api/games/<int:pk>', views.GameDetail.as_view(), name="games-detail"),
    # re_path(r'^api/games/<int:pk>/odds/$', views.GameOddsViewSet, name="gameodds-detail"),
    # path('api/sports', views.SportList.as_view(), name="sports-list"),
    # path('api/regions', views.RegionList.as_view(), name="regions-list"),
    # path('api/regions/<int:pk>', views.RegionDetail.as_view(), name="regions-detail"),
    # path('api/leagues', views.LeagueList.as_view(), name="leagues-list"),
    # path('api/leagues/<int:pk>', views.LeagueDetail.as_view(), name="leagues-detail"),
    # path('api/sources', views.OddsSourceList.as_view(), name="sources-list"),
    # path('api/sources/<int:pk>', views.OddsSourceDetail.as_view(), name="sources-detail"),
    # path('api/odds', views.OddsList.as_view(), name="odds-list"),
    # path('api/game-odds', views.GameOddsList.as_view(), name="game-odds")
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/games/', views.GameList.as_view(), name="games-list"),
#     re_path(r'^api/games/$', views.GameList.as_view(), name="games-list"),
#     path('api/games/<int:pk>', views.GameDetail.as_view(), name="games-detail"),
#     path('api/games/<int:pk>/odds', views.GameOddsDetail.as_view(), name="gameodds-detail"),
#     path('api/sports', views.SportList.as_view(), name="sports-list"),
#     path('api/sports/<int:pk>', views.SportDetail.as_view(), name="sports-detail"),
#     path('api/regions', views.RegionList.as_view(), name="regions-list"),
#     path('api/regions/<int:pk>', views.RegionDetail.as_view(), name="regions-detail"),
#     path('api/leagues', views.LeagueList.as_view(), name="leagues-list"),
#     path('api/leagues/<int:pk>', views.LeagueDetail.as_view(), name="leagues-detail"),
#     path('api/sources', views.OddsSourceList.as_view(), name="sources-list"),
#     path('api/sources/<int:pk>', views.OddsSourceDetail.as_view(), name="sources-detail"),
#     path('api/odds', views.OddsList.as_view(), name="odds-list"),
#     path('api/game-odds', views.GameOddsList.as_view(), name="game-odds")
# ]

urlpatterns = format_suffix_patterns(urlpatterns)

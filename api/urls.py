from django.urls import path

from api.views.down import FileDownMaqolaView, FileDownAsarView, FileDownTadqiqotView, FileDownSherView, \
    FileDownHotiraView, FileDownArxiv_hujjatView, FileDownDissertatsiyaView, FileDownSahifaView
from api.views.foydali_havolalar import Foydali_havolalarListView, foydali_havolalardetail
from api.views.full_text_search import full_text_search
from api.views.hikmatli_sozlar import Hikmatli_sozlarListView, hikmatli_sozlardetail
from api.views.hujjatlar import AsarlarListView, asarlardetail, MaqolalarListView, maqolalardetail, TadqiqotlarListView, \
    tadqiqotlardetail, SherlarListView, sherlardetail, HotiralarListView, hotiralardetail, Arxiv_hujjatlarListView, \
    arxiv_hujjatlardetail, DissertatsiyaListView, dissertatsiyadetail
from api.views.ishtirokchilar import IshtirokchilarListView, ishtirokchilardetail
from api.views.jadidlar import JadidlarListView, jadidlardetail
from api.views.manbalar import AudiolarListView, audiolardetail, VideolarListView, videolardetail, RasmlarListView, \
    rasmlardetail
from api.views.sahifalar import SahifalarListView, sahifalardetail
from api.views.slayder import SlayderListView, slayderdetail
from api.views.tadbirlar import KanferensiyalarListView, kanferensiyalardetail, SeminarlarListView, seminarlardetail, \
    YangiliklarListView, yangiliklardetail
from api.views.tanlovlar import TanlovlarListView, tanlovlardetail
# from rest_framework_simplejwt import views as jwt_views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


    path('foydali_havolalar/', Foydali_havolalarListView.as_view(), name='foydali_havolalar-list'),
    path('foydali_havolalar/<int:pk>/', foydali_havolalardetail, name='foydali_havolalar-detail'),

    path('hikmatli_sozlar/', Hikmatli_sozlarListView.as_view(), name='hikmatli_sozlar-list'),
    path('hikmatli_sozlar/<int:pk>/', hikmatli_sozlardetail, name='hikmatli_sozlar-detail'),

    path('asarlar/', AsarlarListView.as_view(), name='asarlar-list'),
    path('asarlar/<int:pk>/', asarlardetail, name='asarlar-detail'),

    path('maqolalar/', MaqolalarListView.as_view(), name='maqolalar-list'),
    path('maqolalar/<int:pk>/', maqolalardetail, name='maqolalar-detail'),

    path('tadqiqotlar/', TadqiqotlarListView.as_view(), name='tadqiqotlar-list'),
    path('tadqiqotlar/<int:pk>/', tadqiqotlardetail, name='tadqiqotlar-detail'),

    path('sherlar/', SherlarListView.as_view(), name='sherlar-list'),
    path('sherlar/<int:pk>/', sherlardetail, name='sherlar-detail'),

    path('hotiralar/', HotiralarListView.as_view(), name='hotiralar-list'),
    path('hotiralar/<int:pk>/', hotiralardetail, name='hotiralar-detail'),

    path('arxiv_hujjatlar/', Arxiv_hujjatlarListView.as_view(), name='arxiv_hujjatlar-list'),
    path('arxiv_hujjatlar/<int:pk>/', arxiv_hujjatlardetail, name='arxiv_hujjatlar-detail'),

    path('dissertatsiya/', DissertatsiyaListView.as_view(), name='dissertatsiya-list'),
    path('dissertatsiya/<int:pk>/', dissertatsiyadetail, name='dissertatsiya-detail'),

    path('ishtirokchilar/', IshtirokchilarListView.as_view(), name='ishtirokchilar-list'),
    path('ishtirokchilar/<int:pk>/', ishtirokchilardetail, name='ishtirokchilar-detail'),

    path('jadidlar/', JadidlarListView.as_view(), name='jadidlar-list'),
    path('jadidlar/<int:pk>/', jadidlardetail, name='jadidlar-detail'),

    path('audiolar/', AudiolarListView.as_view(), name='audiolar-list'),
    path('audiolar/<int:pk>/', audiolardetail, name='audiolar-detail'),

    path('videolar/', VideolarListView.as_view(), name='videolar-list'),
    path('videolar/<int:pk>/', videolardetail, name='videolar-detail'),

    path('rasmlar/', RasmlarListView.as_view(), name='rasmlar-list'),
    path('rasmlar/<int:pk>/', rasmlardetail, name='rasmlar-detail'),

    path('sahifalar/', SahifalarListView.as_view(), name='sahifalar-list'),
    path('sahifalar/<int:pk>/', sahifalardetail, name='sahifalar-detail'),

    path('slayder/', SlayderListView.as_view(), name='slayder-list'),
    path('slayder/<int:pk>/', slayderdetail, name='slayder-detail'),

    path('kanferensiyalar/', KanferensiyalarListView.as_view(), name='kanferensiyalar-list'),
    path('kanferensiyalar/<int:pk>/', kanferensiyalardetail, name='kanferensiyalar-detail'),

    path('seminarlar/', SeminarlarListView.as_view(), name='seminarlar-list'),
    path('seminarlar/<int:pk>/', seminarlardetail, name='seminarlar-detail'),

    path('yangiliklar/', YangiliklarListView.as_view(), name='yangiliklar-list'),
    path('yangiliklar/<int:pk>/', yangiliklardetail, name='yangiliklar-detail'),

    path('tanlovlar/', TanlovlarListView.as_view(), name='tanlovlar-list'),
    path('tanlovlar/<int:pk>/', tanlovlardetail, name='tanlovlar-detail'),


    path('search/', full_text_search, name='search'),


    path('asarlar/downland/<int:pk>/', FileDownAsarView.as_view(), name='asarlar_downland'),
    path('maqolalar/downland/<int:pk>/', FileDownMaqolaView.as_view(), name='maqolalar_downland'),
    path('tadqiqotlar/downland/<int:pk>/', FileDownTadqiqotView.as_view(), name='tadqiqotlar_downland'),
    path('sherlar/downland/<int:pk>/', FileDownSherView.as_view(), name='sherlar_downland'),
    path('hotiralar/downland/<int:pk>/', FileDownHotiraView.as_view(), name='hotiralar_downland'),
    path('arxiv_hujjatlar/downland/<int:pk>/', FileDownArxiv_hujjatView.as_view(), name='arxiv_hujjatlar_downland'),
    path('dissertatsiya/downland/<int:pk>/', FileDownDissertatsiyaView.as_view(), name='dissertatsiya_downland'),
    path('sahifalar/downland/<int:pk>/', FileDownSahifaView.as_view(), name='sahifalar_downland'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
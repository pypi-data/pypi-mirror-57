from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QHBoxLayout

from folderplay.constants import NOT_AVAILABLE
from folderplay.gui.button import ScalablePushButton
from folderplay.gui.groupbox import NoTitleGroupBox
from folderplay.gui.icons import IconSet
from folderplay.gui.label import QIconLabel, DurationLabel, MarqueeLabel
from folderplay.gui.progressbar import BidirectionalProgressBar


class BasicViewWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Play button
        self.btn_play = ScalablePushButton(self)
        self.setup_play_button()

        # Advanced view button
        self.btn_advanced = ScalablePushButton(self)
        self.setup_advanced_button()

        self.btn_refresh = ScalablePushButton(self)
        self.setup_refresh_button()

        # Progressbar
        self.pbr_watched = BidirectionalProgressBar(self)
        self.setup_progress_bar()

        # Media info groupbox
        self.grp_current_media = NoTitleGroupBox(self)
        self.setup_current_media_group_box()

        self.lbl_movie_info_time = DurationLabel(
            0,
            DurationLabel.DisplayMode.endtime,
            IconSet.current.clock,
            NOT_AVAILABLE,
            self,
        )
        self.lbl_movie_info_size = QIconLabel(
            IconSet.current.size, NOT_AVAILABLE, self
        )
        self.lbl_movie_info_size.setToolTip("Media size")

        self.lbl_movie_info_res = QIconLabel(
            IconSet.current.monitor, NOT_AVAILABLE, self
        )
        self.lbl_movie_info_res.setToolTip("Media resolution")

        self.lbl_movie_info_title_icon = QIconLabel(self)
        self.lbl_movie_info_title_icon.setIcon(IconSet.current.movie)
        self.lbl_movie_info_title_icon.setSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed
        )

        self.lbl_movie_info_title = MarqueeLabel(NOT_AVAILABLE, self)
        title_font = self.lbl_movie_info_title.font()
        title_font.setBold(True)
        # title_font.setUnderline(True)
        self.lbl_movie_info_title.setFont(title_font)
        self.setLayout(self.get_layout())
        self.layout().setContentsMargins(0, 0, 0, 0)

    def get_layout(self):
        vlayout = QVBoxLayout()
        vlayout_refresh_advanced = QVBoxLayout()

        hlayout = QHBoxLayout()

        hlayout_info = QHBoxLayout()
        hlayout_info.addWidget(self.lbl_movie_info_time)
        hlayout_info.addWidget(self.lbl_movie_info_size)
        hlayout_info.addWidget(self.lbl_movie_info_res)
        hlayout_title = QHBoxLayout()
        hlayout_title.addWidget(self.lbl_movie_info_title_icon)
        hlayout_title.addWidget(self.lbl_movie_info_title)

        mediainfo_layout_v = QVBoxLayout()
        mediainfo_layout_v.addLayout(hlayout_title)
        mediainfo_layout_v.addLayout(hlayout_info)
        # lbl_movie_info_title
        self.grp_current_media.setLayout(mediainfo_layout_v)

        widgets = [self.btn_advanced, self.btn_refresh]
        for w in widgets:
            vlayout_refresh_advanced.addWidget(w)

        hlayout.addWidget(self.pbr_watched)
        hlayout.addLayout(vlayout_refresh_advanced)

        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.grp_current_media)
        vlayout.addWidget(self.btn_play)
        return vlayout

    def setup_play_button(self):
        icon = IconSet.current.play
        self.btn_play.setIcon(icon)
        self.btn_play.setIconSize(QSize(100, 100))
        self.btn_play.setDefault(True)

    def setup_advanced_button(self):
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.btn_advanced.setSizePolicy(size_policy)
        self.btn_advanced.setToolTip("Advanced options")
        self.btn_advanced.setCheckable(True)
        self.btn_advanced.setIcon(IconSet.current.settings)

    def setup_refresh_button(self):
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.btn_refresh.setSizePolicy(size_policy)
        self.btn_refresh.setToolTip("Refresh")
        self.btn_refresh.setIcon(IconSet.current.refresh)

    def setup_progress_bar(self):
        # Allow pbr_watched to expand to take up all space in layout
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pbr_watched.setSizePolicy(size_policy)
        self.pbr_watched.setAlignment(Qt.AlignHCenter)
        font = self.pbr_watched.font()
        font.setPointSize(25)
        font.setBold(True)
        self.pbr_watched.setFont(font)

    def setup_current_media_group_box(self):
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.grp_current_media.setSizePolicy(size_policy)
        self.grp_current_media.setContextMenuPolicy(Qt.CustomContextMenu)

from slmgen.slmwindow import SLMdialog


def test_dialog(qtbot):
    w = SLMdialog()
    qtbot.addWidget(w)
    w.previewPattern()

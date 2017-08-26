# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/DMT-git/src/ui/ui_proposals.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProposalsDlg(object):
    def setupUi(self, ProposalsDlg):
        ProposalsDlg.setObjectName("ProposalsDlg")
        ProposalsDlg.resize(785, 505)
        ProposalsDlg.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProposalsDlg)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblMessage = QtWidgets.QLabel(ProposalsDlg)
        self.lblMessage.setText("")
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout.addWidget(self.lblMessage)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnRefreshProposals = QtWidgets.QPushButton(ProposalsDlg)
        self.btnRefreshProposals.setAutoDefault(False)
        self.btnRefreshProposals.setObjectName("btnRefreshProposals")
        self.horizontalLayout.addWidget(self.btnRefreshProposals)
        self.btnColumnsProposals = QtWidgets.QPushButton(ProposalsDlg)
        self.btnColumnsProposals.setAutoDefault(False)
        self.btnColumnsProposals.setObjectName("btnColumnsProposals")
        self.horizontalLayout.addWidget(self.btnColumnsProposals)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(ProposalsDlg)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.propsView = QtWidgets.QTableView(self.splitter)
        self.propsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.propsView.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.propsView.setAlternatingRowColors(True)
        self.propsView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.propsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.propsView.setShowGrid(True)
        self.propsView.setSortingEnabled(True)
        self.propsView.setObjectName("propsView")
        self.propsView.verticalHeader().setVisible(True)
        self.propsView.verticalHeader().setCascadingSectionResizes(False)
        self.propsView.verticalHeader().setHighlightSections(False)
        self.tabsDetails = QtWidgets.QTabWidget(self.splitter)
        self.tabsDetails.setObjectName("tabsDetails")
        self.tabDetails = QtWidgets.QWidget()
        self.tabDetails.setStyleSheet("")
        self.tabDetails.setObjectName("tabDetails")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabDetails)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblDetailsPaymentAmountLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsPaymentAmountLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsPaymentAmountLabel.setObjectName("lblDetailsPaymentAmountLabel")
        self.gridLayout_2.addWidget(self.lblDetailsPaymentAmountLabel, 4, 0, 1, 1)
        self.lblDetailsUrlLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsUrlLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsUrlLabel.setObjectName("lblDetailsUrlLabel")
        self.gridLayout_2.addWidget(self.lblDetailsUrlLabel, 1, 0, 1, 1)
        self.lblDetailsVotingStatusLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsVotingStatusLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsVotingStatusLabel.setObjectName("lblDetailsVotingStatusLabel")
        self.gridLayout_2.addWidget(self.lblDetailsVotingStatusLabel, 3, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblDetailsPaymentStart = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsPaymentStart.setOpenExternalLinks(True)
        self.lblDetailsPaymentStart.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsPaymentStart.setObjectName("lblDetailsPaymentStart")
        self.horizontalLayout_8.addWidget(self.lblDetailsPaymentStart)
        self.lblDetailsPaymentEndLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsPaymentEndLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsPaymentEndLabel.setObjectName("lblDetailsPaymentEndLabel")
        self.horizontalLayout_8.addWidget(self.lblDetailsPaymentEndLabel)
        self.lblDetailsPaymentEnd = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsPaymentEnd.setOpenExternalLinks(True)
        self.lblDetailsPaymentEnd.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsPaymentEnd.setObjectName("lblDetailsPaymentEnd")
        self.horizontalLayout_8.addWidget(self.lblDetailsPaymentEnd)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 6, 1, 1, 1)
        self.lblDetailsName = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsName.setOpenExternalLinks(True)
        self.lblDetailsName.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsName.setObjectName("lblDetailsName")
        self.gridLayout_2.addWidget(self.lblDetailsName, 0, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblDetailsPaymentAmount = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsPaymentAmount.setOpenExternalLinks(True)
        self.lblDetailsPaymentAmount.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsPaymentAmount.setObjectName("lblDetailsPaymentAmount")
        self.horizontalLayout_7.addWidget(self.lblDetailsPaymentAmount)
        self.lblDetailsPaymentAddressLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsPaymentAddressLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsPaymentAddressLabel.setObjectName("lblDetailsPaymentAddressLabel")
        self.horizontalLayout_7.addWidget(self.lblDetailsPaymentAddressLabel)
        self.lblDetailsPaymentAddress = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsPaymentAddress.setOpenExternalLinks(True)
        self.lblDetailsPaymentAddress.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsPaymentAddress.setObjectName("lblDetailsPaymentAddress")
        self.horizontalLayout_7.addWidget(self.lblDetailsPaymentAddress)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 4, 1, 1, 1)
        self.lblDetailsUrl = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsUrl.setOpenExternalLinks(True)
        self.lblDetailsUrl.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsUrl.setObjectName("lblDetailsUrl")
        self.gridLayout_2.addWidget(self.lblDetailsUrl, 1, 1, 1, 1)
        self.lblDetailsNameLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsNameLabel.setObjectName("lblDetailsNameLabel")
        self.gridLayout_2.addWidget(self.lblDetailsNameLabel, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.lblDetailsCreationTime = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsCreationTime.setObjectName("lblDetailsCreationTime")
        self.gridLayout_2.addWidget(self.lblDetailsCreationTime, 2, 1, 1, 1)
        self.lblDetailsPaymentStartLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsPaymentStartLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsPaymentStartLabel.setObjectName("lblDetailsPaymentStartLabel")
        self.gridLayout_2.addWidget(self.lblDetailsPaymentStartLabel, 6, 0, 1, 1)
        self.lblDetailsCreationTimeLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsCreationTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsCreationTimeLabel.setObjectName("lblDetailsCreationTimeLabel")
        self.gridLayout_2.addWidget(self.lblDetailsCreationTimeLabel, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblDetailsVotingStatus = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsVotingStatus.setOpenExternalLinks(True)
        self.lblDetailsVotingStatus.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsVotingStatus.setObjectName("lblDetailsVotingStatus")
        self.horizontalLayout_6.addWidget(self.lblDetailsVotingStatus)
        self.lblDetailsYesCountLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsYesCountLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsYesCountLabel.setObjectName("lblDetailsYesCountLabel")
        self.horizontalLayout_6.addWidget(self.lblDetailsYesCountLabel)
        self.lblDetailsYesCount = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsYesCount.setOpenExternalLinks(True)
        self.lblDetailsYesCount.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsYesCount.setObjectName("lblDetailsYesCount")
        self.horizontalLayout_6.addWidget(self.lblDetailsYesCount)
        self.lblDetailsNoCountLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsNoCountLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsNoCountLabel.setObjectName("lblDetailsNoCountLabel")
        self.horizontalLayout_6.addWidget(self.lblDetailsNoCountLabel)
        self.lblDetailsNoCount = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsNoCount.setOpenExternalLinks(True)
        self.lblDetailsNoCount.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsNoCount.setObjectName("lblDetailsNoCount")
        self.horizontalLayout_6.addWidget(self.lblDetailsNoCount)
        self.lblDetailsAbstainCountLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsAbstainCountLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsAbstainCountLabel.setObjectName("lblDetailsAbstainCountLabel")
        self.horizontalLayout_6.addWidget(self.lblDetailsAbstainCountLabel)
        self.lblDetailsAbstainCount = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsAbstainCount.setOpenExternalLinks(True)
        self.lblDetailsAbstainCount.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsAbstainCount.setObjectName("lblDetailsAbstainCount")
        self.horizontalLayout_6.addWidget(self.lblDetailsAbstainCount)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 1, 1, 1)
        self.lblDetailsProposalHashLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsProposalHashLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsProposalHashLabel.setObjectName("lblDetailsProposalHashLabel")
        self.gridLayout_2.addWidget(self.lblDetailsProposalHashLabel, 7, 0, 1, 1)
        self.lblDetailsCollateralHashLabel = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsCollateralHashLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDetailsCollateralHashLabel.setObjectName("lblDetailsCollateralHashLabel")
        self.gridLayout_2.addWidget(self.lblDetailsCollateralHashLabel, 8, 0, 1, 1)
        self.lblDetailsProposalHash = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsProposalHash.setOpenExternalLinks(True)
        self.lblDetailsProposalHash.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsProposalHash.setObjectName("lblDetailsProposalHash")
        self.gridLayout_2.addWidget(self.lblDetailsProposalHash, 7, 1, 1, 1)
        self.lblDetailsCollateralHash = QtWidgets.QLabel(self.tabDetails)
        self.lblDetailsCollateralHash.setOpenExternalLinks(True)
        self.lblDetailsCollateralHash.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblDetailsCollateralHash.setObjectName("lblDetailsCollateralHash")
        self.gridLayout_2.addWidget(self.lblDetailsCollateralHash, 8, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.tabsDetails.addTab(self.tabDetails, "")
        self.tabVoting = QtWidgets.QWidget()
        self.tabVoting.setObjectName("tabVoting")
        self.tabsDetails.addTab(self.tabVoting, "")
        self.tabVoteList = QtWidgets.QWidget()
        self.tabVoteList.setObjectName("tabVoteList")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabVoteList)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.votesSplitter = QtWidgets.QSplitter(self.tabVoteList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.votesSplitter.sizePolicy().hasHeightForWidth())
        self.votesSplitter.setSizePolicy(sizePolicy)
        self.votesSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.votesSplitter.setObjectName("votesSplitter")
        self.layoutWidget = QtWidgets.QWidget(self.votesSplitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutVotesView = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layoutVotesView.setContentsMargins(0, 0, 0, 0)
        self.layoutVotesView.setSpacing(2)
        self.layoutVotesView.setObjectName("layoutVotesView")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnReloadVotes = QtWidgets.QPushButton(self.layoutWidget)
        self.btnReloadVotes.setObjectName("btnReloadVotes")
        self.horizontalLayout_2.addWidget(self.btnReloadVotes)
        self.chbOnlyMyVotes = QtWidgets.QCheckBox(self.layoutWidget)
        self.chbOnlyMyVotes.setToolTip("")
        self.chbOnlyMyVotes.setObjectName("chbOnlyMyVotes")
        self.horizontalLayout_2.addWidget(self.chbOnlyMyVotes)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.layoutVotesView.addLayout(self.horizontalLayout_2)
        self.layoutVotesViewFilter = QtWidgets.QHBoxLayout()
        self.layoutVotesViewFilter.setSpacing(8)
        self.layoutVotesViewFilter.setObjectName("layoutVotesViewFilter")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.layoutVotesViewFilter.addWidget(self.label_2)
        self.edtVotesViewFilter = QtWidgets.QLineEdit(self.layoutWidget)
        self.edtVotesViewFilter.setObjectName("edtVotesViewFilter")
        self.layoutVotesViewFilter.addWidget(self.edtVotesViewFilter)
        self.btnApplyVotesViewFilter = QtWidgets.QPushButton(self.layoutWidget)
        self.btnApplyVotesViewFilter.setObjectName("btnApplyVotesViewFilter")
        self.layoutVotesViewFilter.addWidget(self.btnApplyVotesViewFilter)
        self.layoutVotesView.addLayout(self.layoutVotesViewFilter)
        self.votesView = QtWidgets.QTableView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.votesView.sizePolicy().hasHeightForWidth())
        self.votesView.setSizePolicy(sizePolicy)
        self.votesView.setObjectName("votesView")
        self.layoutVotesView.addWidget(self.votesView)
        self.widget = QtWidgets.QWidget(self.votesSplitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.votesSplitter)
        self.tabsDetails.addTab(self.tabVoteList, "")
        self.tabWebPreview = QtWidgets.QWidget()
        self.tabWebPreview.setObjectName("tabWebPreview")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabWebPreview)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layoutWebPreview = QtWidgets.QVBoxLayout()
        self.layoutWebPreview.setObjectName("layoutWebPreview")
        self.layoutURL = QtWidgets.QHBoxLayout()
        self.layoutURL.setObjectName("layoutURL")
        self.label = QtWidgets.QLabel(self.tabWebPreview)
        self.label.setObjectName("label")
        self.layoutURL.addWidget(self.label)
        self.edtURL = QtWidgets.QLineEdit(self.tabWebPreview)
        self.edtURL.setReadOnly(True)
        self.edtURL.setObjectName("edtURL")
        self.layoutURL.addWidget(self.edtURL)
        self.layoutWebPreview.addLayout(self.layoutURL)
        self.verticalLayout_3.addLayout(self.layoutWebPreview)
        self.tabsDetails.addTab(self.tabWebPreview, "")
        self.verticalLayout.addWidget(self.splitter)
        self.buttonBox = QtWidgets.QDialogButtonBox(ProposalsDlg)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProposalsDlg)
        self.tabsDetails.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProposalsDlg)

    def retranslateUi(self, ProposalsDlg):
        _translate = QtCore.QCoreApplication.translate
        ProposalsDlg.setWindowTitle(_translate("ProposalsDlg", "Dialog"))
        self.btnRefreshProposals.setText(_translate("ProposalsDlg", "Refresh"))
        self.btnColumnsProposals.setText(_translate("ProposalsDlg", "Columns..."))
        self.lblDetailsPaymentAmountLabel.setText(_translate("ProposalsDlg", "Payment amount:"))
        self.lblDetailsUrlLabel.setText(_translate("ProposalsDlg", "URL:"))
        self.lblDetailsVotingStatusLabel.setText(_translate("ProposalsDlg", "Voting:"))
        self.lblDetailsPaymentStart.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsPaymentEndLabel.setText(_translate("ProposalsDlg", "end:"))
        self.lblDetailsPaymentEnd.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsName.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsPaymentAmount.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsPaymentAddressLabel.setText(_translate("ProposalsDlg", "address:"))
        self.lblDetailsPaymentAddress.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsUrl.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsNameLabel.setText(_translate("ProposalsDlg", "Name:"))
        self.lblDetailsCreationTime.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsPaymentStartLabel.setText(_translate("ProposalsDlg", "Payment start:"))
        self.lblDetailsCreationTimeLabel.setText(_translate("ProposalsDlg", "Creation time:"))
        self.lblDetailsVotingStatus.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsYesCountLabel.setText(_translate("ProposalsDlg", "Yes:"))
        self.lblDetailsYesCount.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsNoCountLabel.setText(_translate("ProposalsDlg", "No:"))
        self.lblDetailsNoCount.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsAbstainCountLabel.setText(_translate("ProposalsDlg", "Abstain:"))
        self.lblDetailsAbstainCount.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsProposalHashLabel.setText(_translate("ProposalsDlg", "Proposal hash:"))
        self.lblDetailsCollateralHashLabel.setText(_translate("ProposalsDlg", "Collateral hash:"))
        self.lblDetailsProposalHash.setText(_translate("ProposalsDlg", "--"))
        self.lblDetailsCollateralHash.setText(_translate("ProposalsDlg", "--"))
        self.tabsDetails.setTabText(self.tabsDetails.indexOf(self.tabDetails), _translate("ProposalsDlg", "Details"))
        self.tabsDetails.setTabText(self.tabsDetails.indexOf(self.tabVoting), _translate("ProposalsDlg", "Vote"))
        self.btnReloadVotes.setToolTip(_translate("ProposalsDlg", "Reads new votes from the Dash network"))
        self.btnReloadVotes.setText(_translate("ProposalsDlg", "Refresh"))
        self.chbOnlyMyVotes.setText(_translate("ProposalsDlg", "Show my votes only"))
        self.label_2.setText(_translate("ProposalsDlg", "Filter:"))
        self.btnApplyVotesViewFilter.setText(_translate("ProposalsDlg", "Apply"))
        self.tabsDetails.setTabText(self.tabsDetails.indexOf(self.tabVoteList), _translate("ProposalsDlg", "Voting History"))
        self.label.setText(_translate("ProposalsDlg", "URL: "))
        self.tabsDetails.setTabText(self.tabsDetails.indexOf(self.tabWebPreview), _translate("ProposalsDlg", "Web Page Preview"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProposalsDlg = QtWidgets.QDialog()
    ui = Ui_ProposalsDlg()
    ui.setupUi(ProposalsDlg)
    ProposalsDlg.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-
"""
QtCore backport module.
"""
from os.path import dirname
from warnings import warn
from sys import path

if dirname(__file__) not in path:
    path.append(dirname(__file__))
if dirname(dirname(__file__)) not in path:
    path.append(dirname(dirname(__file__)))

try:
    from .._api import USED_API, QT_API_PYQT5
except:
    try:
        from ._api import USED_API, QT_API_PYQT5
    except:
        from _api import USED_API, QT_API_PYQT5

assert USED_API is QT_API_PYQT5
from PyQt5.QtCore import (
    PYQT_CONFIGURATION,
    PYQT_VERSION,
    PYQT_VERSION_STR,
    QAbstractAnimation,
    QAbstractEventDispatcher,
    # QAbstractFileEngine,
    # QAbstractFileEngineHandler,
    # QAbstractFileEngineIterator,
    QAbstractItemModel,
    QAbstractListModel,
    QAbstractState,
    QAbstractTableModel,
    QAbstractTransition,
    QAnimationGroup,
    QBasicTimer,
    QBitArray,
    QBuffer,
    QByteArray,
    QByteArrayMatcher,
    QChildEvent,
    QCoreApplication,
    QCryptographicHash,
    QDataStream,
    QDate,
    QDateTime,
    QDir,
    QDirIterator,
    QDynamicPropertyChangeEvent,
    QEasingCurve,
    QElapsedTimer,
    QEvent,
    QEventLoop,
    QEventTransition,
    # QFSFileEngine,
    QFile,
    QFileInfo,
    QFileSystemWatcher,
    QFinalState,
    QGenericArgument,
    QGenericReturnArgument,
    QHistoryState,
    QIODevice,
    QLibrary,
    QLibraryInfo,
    QLine,
    QLineF,
    QLocale,
    QMargins,
    QMetaClassInfo,
    QMetaEnum,
    QMetaMethod,
    QMetaObject,
    QMetaProperty,
    QMetaType,
    QMimeData,
    QModelIndex,
    QMutex,
    QMutexLocker,
    QObject,
    QObjectCleanupHandler,
    QParallelAnimationGroup,
    QPauseAnimation,
    QPersistentModelIndex,
    QPluginLoader,
    QPoint,
    QPointF,
    QProcess,
    QProcessEnvironment,
    QPropertyAnimation,
    # QPyNullVariant,
    QReadLocker,
    QReadWriteLock,
    QRect,
    QRectF,
    QRegExp,
    QResource,
    QRunnable,
    QSemaphore,
    QSequentialAnimationGroup,
    QSettings,
    QSharedMemory,
    QSignalMapper,
    QSignalTransition,
    QSize,
    QSizeF,
    QSocketNotifier,
    QState,
    QStateMachine,
    QSysInfo,
    # QSystemLocale,
    QSystemSemaphore,
    QT_TRANSLATE_NOOP,
    QT_TR_NOOP,
    QT_TR_NOOP_UTF8,
    QT_VERSION,
    QT_VERSION_STR,
    QTemporaryFile,
    QTextBoundaryFinder,
    QTextCodec,
    QTextDecoder,
    QTextEncoder,
    QTextStream,
    QTextStreamManipulator,
    QThread,
    QThreadPool,
    QTime,
    QTimeLine,
    QTimer,
    QTimerEvent,
    QTranslator,
    QUrl,
    QUuid,
    QVariant,
    QVariantAnimation,
    QWaitCondition,
    QWriteLocker,
    QXmlStreamAttribute,
    QXmlStreamAttributes,
    QXmlStreamEntityDeclaration,
    QXmlStreamEntityResolver,
    QXmlStreamNamespaceDeclaration,
    QXmlStreamNotationDeclaration,
    QXmlStreamReader,
    QXmlStreamWriter,
    Q_ARG,
    Q_CLASSINFO,
    Q_ENUMS,
    Q_FLAGS,
    Q_RETURN_ARG,
    Qt,
    QtCriticalMsg,
    QtDebugMsg,
    QtFatalMsg,
    QtMsgType,
    QtSystemMsg,
    QtWarningMsg,
    # SIGNAL,
    # SLOT,
    bin_,
    bom,
    center,
    dec,
    endl,
    fixed,
    flush,
    forcepoint,
    forcesign,
    hex_,
    left,
    lowercasebase,
    lowercasedigits,
    noforcepoint,
    noforcesign,
    noshowbase,
    oct_,
    pyqtBoundSignal,
    pyqtPickleProtocol,
    pyqtProperty,
    pyqtRemoveInputHook,
    pyqtRestoreInputHook,
    pyqtSetPickleProtocol,
    pyqtSignal,
    # pyqtSignature,
    pyqtSlot,
    # pyqtWrapperType,
    qAbs,
    qAddPostRoutine,
    qChecksum,
    qCompress,
    qCritical,
    qDebug,
    qErrnoWarning,
    qFatal,
    qFuzzyCompare,
    qInf,
    # qInstallMsgHandler,
    qIsFinite,
    qIsInf,
    qIsNaN,
    qIsNull,
    qQNaN,
    qRegisterResourceData,
    qRemovePostRoutine,
    qRound,
    qRound64,
    qSNaN,
    qSetFieldWidth,
    qSetPadChar,
    qSetRealNumberPrecision,
    qSharedBuild,
    # qSwap,
    qUncompress,
    qUnregisterResourceData,
    qVersion,
    qWarning,
    qrand,
    qsrand,
    reset,
    right,
    scientific,
    showbase,
    uppercasebase,
    uppercasedigits,
    ws
)

from PyQt5.QtCore import qInstallMessageHandler as _qInstallMessageHandler, QUrlQuery as _QUrlQuery

__missing__ = [
    'QAbstractFileEngine',
    'QAbstractFileEngineHandler',
    'QAbstractFileEngineIterator',
    'QFSFileEngine',
    'QPyNullVariant',
    'QSystemLocale'
    "SIGNAL",
    "SLOT",
    "pyqtSignature",
    "qInstallMsgHandler",
    "qSwap"
]  # type: list[str]

try:
    from ._utils import obsolete_rename as _obsolete_rename
except:
    from _utils import obsolete_rename as _obsolete_rename


def qInstallMsgHandler(func):
    """
    :param func: callable | None
    :return: callable | None
    """
    wrapped = lambda msgtype, context, text: func(msgtype, text)
    old = getattr(qInstallMsgHandler, "_handler", None)
    if func is not None:
        _qInstallMessageHandler(wrapped)
    else:
        _qInstallMessageHandler(None)
    qInstallMsgHandler._handler = func
    return old


def _QMetaMethod_signature(self):
    """
    :param self: QMetaMethod
    :return: bytes
    """
    # Return the method signature as bytes
    return bytes(self.methodSignature())


QMetaMethod.signature = _QMetaMethod_signature

SIGNAL = lambda str_: QMetaObject.normalizedSignature(str_)
SLOT = lambda str_: QMetaObject.normalisedSignature(str_)


def _QObject_emit(self, sig, *args):
    """
    :param sig: str | unicode
    :param args: any
    :return: bool
    """
    warn("QObject.emit is obsolete and is removed in PyQt5. Use new style signal.emit(...)", stacklevel=2)
    meta = self.metaObject()
    sIndex = meta.indexOfSignal(sig)
    if sIndex == -1:
        warn("No signal '{}' defined in {}".format(sig, type(self).__name__), stacklevel=2)
        return False
    method = meta.method(sIndex)
    return method.invoke(self, Qt.DirectConnection, *[Q_ARG(type(a), a) for a in args])

QObject.emit = _QObject_emit
QRectF.intersect = _obsolete_rename("QRectF.intersect", QRectF.intersected)
QRectF.unite = _obsolete_rename("QRectF.unite", QRectF.united)
QRect.intersect = _obsolete_rename("QRect.intersect", QRect.intersected)
QRect.unite = _obsolete_rename("QRect.unite", QRect.united)

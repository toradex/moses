import QtQuick 2.0
import QtQuick.Controls 2.0

Rectangle {
    width: 200
    height: 200
    color: "green"

    Text {
        id: mytext
        objectName: "mytext"
        text: "Hello World"
        anchors.verticalCenterOffset: -56
        anchors.horizontalCenterOffset: 1
        anchors.centerIn: parent
    }

    Button {
        id: mybutton
        x: 51
        y: 109
        objectName: "mybutton"
        text: "Hello"
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.100000023841858}
}
##^##*/

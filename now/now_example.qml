import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.2

ApplicationWindow {
    id: app
    width: 400
    height: 200
    title: qsTr("Example")
    visible: true

    signal updateModel()

    Rectangle {
        anchors.fill: parent; color: "black"

        Text {
            id: messageText
            anchors.centerIn: parent; color: "white"
            text: "Click to update the time."

            Connections {
                target: now_model
                onUpdated: {
                    messageText.text = now_model.timestamp()
                }
            }  
        }

        MouseArea {
            id: mouseArea
            anchors.fill: parent

            onClicked: {
                updateModel()
            }
        }      
    }
}
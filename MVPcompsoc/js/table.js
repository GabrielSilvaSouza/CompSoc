var tableBody = document.getElementById("table-body");
var buttonBack = document.getElementById("button-previous");
var buttonNext = document.getElementById("button-next");

data = [{
    team: "delta",
    date: "hoje",
    status: "disponivel",
    Description: "", 
    Workload: 1,
    Apply: "",
    Comments: ""
    },{
    team: "delta",
    date: "hoje",
    status: "disponivel",
    Description: "", 
    Workload: 1,
    Apply: "",
    Comments: ""
    },{
    team: "delta",
    date: "hoje",
    status: "disponivel",
    Description: "", 
    Workload: 1,
    Apply: "",
    Comments: ""
    }, {
    team: "delta",
    date: "hoje",
    status: "disponivel",
    Description: "", 
    Workload: 1,
    Apply: "",
    Comments: ""
        },{
    team: "delta",
    date: "hoje",
    status: "disponivel",
    Description: "", 
    Workload: 1,
    Apply: "",
    Comments: ""
    },{
    team: "delta",
    date: "hoje",
    status: "disponivel",
    Description: "", 
    Workload: 1,
    Apply: "",
    Comments: ""
    },{
    team: "delta",
    date: "hoje",
    status: "disponivel",
    Description: "", 
    Workload: 1,
    Apply: "",
    Comments: ""
    },{
    team: "delta",
    date: "hoje",
    status: "disponivel",
    Description: "", 
    Workload: 1,
    Apply: "",
    Comments: ""
    },{
    team: "delta",
    date: "hoje",
    status: "disponivel",
    Description: "", 
    Workload: 1,
    Apply: "",
    Comments: ""
    },{
    team: "delta",
    date: "hoje",
    status: "disponivel",
    Description: "", 
    Workload: 1,
    Apply: "",
    Comments: ""
    }];

var html = "";
var count = 0;

function createTable() {

    for (let i = count; i < count+5 && i < data.length; i++) {
        html += "<tr>";
        html += "<td>" + (i+1) + "</td>";
        html += "<td>" + data[count]["team"] + "</td>";
        html += "<td>" + data[count]["date"] + "</td>";
        html += "<td>" + data[count]["status"] + "</td>";
        html += "<td>" + data[count]["Description"] + "</td>";
        html += "<td>" + data[count]["Workload"] + "</td>";
        html += "<td>" + data[count]["Apply"] + "</td>";
        html += "<td>" + data[count]["Comments"] + "</td>";
        html += "</tr>";
    }

    tableBody.innerHTML = html;
}

function updateTable(index) {
    html = "";
    count = index;
    for (let i = count; i < count+5 && i < data.length; i++){
        html += "<tr>";
        html += "<td>" + (i+1) + "</td>";
        html += "<td>" + data[count]["team"] + "</td>";
        html += "<td>" + data[count]["date"] + "</td>";
        html += "<td>" + data[count]["status"] + "</td>";
        html += "<td>" + data[count]["Description"] + "</td>";
        html += "<td>" + data[count]["Workload"] + "</td>";
        html += "<td>" + data[count]["Apply"] + "</td>";
        html += "<td>" + data[count]["Comments"] + "</td>";
        html += "</tr>";
    }

    tableBody.innerHTML = html;
}

createTable();

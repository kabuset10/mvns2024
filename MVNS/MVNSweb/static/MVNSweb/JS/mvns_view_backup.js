var readingList = makeTableToList()
function makeTableToList() {
  var tableObj = document.getElementById( "readingTable" );
  var readingList = [];
  var allTRs = tableObj.getElementsByTagName( "tr" );
  for ( var trCounter = 0; trCounter < allTRs.length; trCounter++ )
  {
     var tmpArr = [];
     var allTDsInTR = allTRs[ trCounter ].getElementsByTagName( "td" );
     for ( var tdCounter = 0; tdCounter < allTDsInTR.length; tdCounter++ )
     {
        tmpArr.push( allTDsInTR[ tdCounter ].innerHTML );
     }
     readingList.push( tmpArr );
  }
  return (readingList);
}

function tableToBlock(tableId) {
  try {
    let thArray = [];
    const readingTable = document.getElementById(tableId);
    const tableHeader = readingTable.getElementsByTagName('th');
    for (let i = 0; i < tableHeader.length; i++) {
      const headerText = tableHeader[i].innerHTML;
      thArray.push(headerText);
    }
    const tableElementStyle = document.createElement('style');
    let tableStyleSheet;
    document.head.appendChild(tableElementStyle);
    tableStyleSheet = tableElementStyle.sheet;
    for (let i = 0; i < thArray.length; i++){
      tableStyleSheet.insertRule(
        '#' +
        tableId +
        ' td:nth-child('
        + (i + 1) +
        ')::before {content:"' +
        thArray[i] +
        ': ";}',
        tableStyleSheet.cssRules.length
      );
    }
  }
  catch (err){
    console.log('tableToBlock(): ' + err);
  }
}
tableToBlock('readingTable');

function makeTableFromList(list){
  var table = document.getElementById('readingTable');
  for (var i = 0; i < list.length; i++){
    var listKey = Object.keys(list[i]);
    var listVal = Object.values(list[i]);
    var newRow = table.insertRow(table.rows.length);
    for (var j = 0; j < listKey.length; j++) {
      newCell = newRow.insertCell(j);
      newCell.innerHTML = listVal[j];
    }
  }
};

document.getElementById('dateFilter').addEventListener("change", filterList);
document.getElementById('timeFromFilter').addEventListener("change", filterList);
document.getElementById('timeToFilter').addEventListener("change", filterList);

function filterList() {
  var dateFilterInput = document.getElementById('dateFilter').value;
  var timeFromFilterInput = document.getElementById('timeFromFilter').value;
  var timeToFilterInput = document.getElementById('timeToFilter').value;
  var filteredList = [];
    for (var i = 0; i < readingList.length; i++) {
      setDataList = readingList[i];
      if ((dateFilterInput === setDataList[1] || dateFilterInput === "") &&
        (timeFromFilterInput <= setDataList[2] || timeFromFilterInput === "") &&
        (timeToFilterInput >= setDataList[2] || timeToFilterInput === "")){
          filteredList.push(setDataList);
        }
      document.getElementById('readingTable').innerHTML = "<table><thead><tr><th>Order No.</th><th>Date</th><th>Time</th><th>Name</th><th>Plate No.</th><th>Calculated dB</th><th>dB Reading</th><th>Distance (cm)</th></tr></thead><tbody><tr></tr></tbody></table>";
      makeTableFromList(filteredList);
      tableToBlock('readingTable')
    }
  console.log(filteredList)
}

function time(id, ind) {
  var currentdate = new Date();
  var min = currentdate.getMinutes();
  if (min < 10) {
    var min = 0 + min;
    var timenow = + currentdate.getHours() + ":0" + min;
  }else{
  var timenow = + currentdate.getHours() + ":" + min;
  }
  visitorList[ind].timeOut = timenow;
  document.getElementById(id).innerHTML = visitorList[ind].timeOut;
}

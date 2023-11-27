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
/*
 * Hides the Table of all Entry row by changing the visibility of an
 * parent elment by the id hiddenbudgettable
 */
function hideTable() {
	$('#hiddenbudgettable').hide();
}

/*
 * Adding a new entry row to the defined tbody table element at the bottom of
 * the list
 */
function addBudgetRow() {
	// Getting the values of the types - select by reading an hidden
	// Element with the id selectTypes in the html page
	if ($('#selectTypes').length != 0) {
		var types = $('#selectTypes').html();
		types = types.split(';');
	}
	var def_type_index = 0;
	if ($('#def_type').length != 0) {
		var def_type = $('#def_type').html();
		if (def_type != -1) {
			for (var i = 0; i < types.length; i++) {
				if (types[i] == def_type) {
					def_type_index = i;
					break;
				}
			}
		}
	}

	// Getting the name-select values from html
	if ($('#selectNames').length != 0)
		var names = $('#selectNames').html();
	names = names.split(';');
	// Getting the default values for Name, Estimation, Cost and State
	var def_name_index = 0;
	if ($('#def_name').length != 0)
		var def_name = $('#def_name').html();
	for (var i = 0; i < names.length; i++) {
		if (names[i] == def_name) {
			def_name_index = i;
			break;
		}
	}
	if ($('#def_est').length != 0)
		var def_est = $('#def_est').html();
	if ($('#def_cost').length != 0)
		var def_cost = $('#def_cost').html();
	if ($('#def_state').length != 0)
		var def_state = $('#def_state').html();

	var tBodyContainer = $('#budget_container');
	// initialise the rowcounter by the current amount of rows
	var trElements = tBodyContainer.children('tr');
	var rowCounter = 1;
	if (trElements && trElements.length > 0) {
		rowCounter = trElements[trElements.length - 1].id.split('-')[1];
		rowCounter++;
	}
	var tableRow = document.createElement('tr');
	// Amount of Columns, may should be given by function call
	var columnCount = 6;
	tableRow.id = 'row-' + rowCounter;
	tBodyContainer.append(tableRow);
	// Adding column by column to the row element
	for (var column = 1; column <= columnCount; column++) {
		if (column == 4 && def_cost == "-1") {
			continue;
		}
		var td = document.createElement('td');
		var columnElement;
		tableRow.appendChild(td);
		switch (column) {
		case 1:
			// Select NAME Column Position 1
			columnElement = getSelect(names);
			columnElement.selectedIndex = def_name_index;
			break;
		case 2:
			// Select TYPES Column Position 2
			columnElement = getSelect(types);
			columnElement.selectedIndex = def_type_index;
			break;
		case 3:
			// Estimation
			columnElement = document.createElement('input');
			columnElement.setAttribute('value', def_est);
			columnElement.size = 10;
			break;
		case 4:
			// Cost
			if (def_cost == "-1") {
				columnElement = document.createElement('input');
				columnElement.size = 10;
				//columnElement.disabled = "disabled"
				columnElement.type = "hidden";
				columnElement.setAttribute('value', '0')
			} else {
				columnElement = document.createElement('input');
				columnElement.setAttribute('value', def_cost);
				columnElement.size = 10;
			}
			break;
		case 5:
			// State
			columnElement = document.createElement('input');
			columnElement.setAttribute('value', def_state);
			columnElement.size = 10;
			break;
		case 6:
			// Comment
			columnElement = document.createElement('input');
			columnElement.size = 60;
			break;
		default:
			break;
		}
		columnElement.name = rowCounter + '-' + column + "-Insert";
		td.appendChild(columnElement);
	}
	// Adding a Delete Button to the end of the row
	var deleteButtonElement = document.createElement('td');
	deleteButtonElement.innerHTML = '<div class="inlinebuttons">'
			+ '<input type="button" style="border-radius: 1em 1em 1em 1em;'
			+ ' font-size: 100%" name="deleteRow' + rowCounter
			+ '" onclick="deleteRow(' + rowCounter
			+ ')" value = "&#x2718"/></div>';
	tableRow.appendChild(deleteButtonElement);
	// Change hidden tbody elment to be visible
	$('#hiddenbudgettable').show();
}

/*
 * Creates a new Select Element with the optionsvalues which were given by the
 * submitted Array
 */
function getSelect(optionArray) {
	if (optionArray == null)
		return null;

	var columnElement = document.createElement('select');
	for (var arrayPosition = 0; arrayPosition < optionArray.length; arrayPosition++) {
		var newOption = document.createElement('option');
		newOption.text = optionArray[arrayPosition];
		try {// standards compliant; doesn't work in IE
			columnElement.add(newOption, null);
		} catch (ex) { // just ie
			columnElement.add(newOption, columnElement.selectedIndex);
		}
	}
	return columnElement
}

/*
 * Marks a Row, by the given rowid, as to delete by adding a style attribut
 * visibility by the value none to the parent tr Element. All fields
 * additionally will gets an Prefix DEL on the beginning of the Name: NewName =
 * DEL + oldName The Prefix DEL is necessary to identify deleted rows in further
 * processing performed by the python plugin
 */
function deleteRow(rowID) {
	if (rowID < 0)
		return;

	var row = $("#row-" + rowID);
	row.hide();
	var rowElems = row.find("select , input");
	for (var i in rowElems) {
		rowElems[i].name = (rowElems[i].name + "").match(/\d+-\d+/) + "-Delete";
	}

	// This logic ist responsible for hidding the complete tbody element, if no
	// further row ist visible or rather not deleted
	if ($('#budget_container').find('tr[style!="display: none;"]').length == 0) {
		hideTable();
	}
}

function update(row, column) {
	if (row < 0 || column < 0)
		return;

	var ename = row + "-" + column;
	$("[name='" + ename + "']").attr('name', ename + '-Update');
}

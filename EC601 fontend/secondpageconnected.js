(function(){
	function init(){
		loadMatchingResult();
	}
	function $(tag, options) {
		if (!options) {
			return document.getElementById(tag);
		}

		var element = document.createElement(tag);

		for ( var option in options) {
			if (options.hasOwnProperty(option)) {
				element[option] = options[option];
			}
		}

		return element;
	}
	function showLoadingMessage(msg) {
		var itemList = $('item-list');
		itemList.innerHTML = '<p class="notice"><i class="fa fa-spinner fa-spin"></i> '+ msg + '</p>';
	}

	function showWarningMessage(msg) {
	    var itemList = $('item-list');
	    itemList.innerHTML = '<p class="notice"><i class="fa fa-exclamation-triangle"></i> ' + msg + '</p>';
	}

	function showErrorMessage(msg) {
		var itemList = $('item-list');
		itemList.innerHTML = '<p class="notice"><i class="fa fa-exclamation-circle"></i> ' + msg + '</p>';
	}
	function ajax(method, url, data, callback, errorHandler) {
		  var xhr = new XMLHttpRequest();

		  xhr.open(method, url, true);

		  xhr.onload = function () {
		    switch (xhr.status) {
		      case 200:
		        callback(xhr.responseText);
		        break;
		      case 403:
		        onSessionInvalid();
		        break;
		      case 401:
		        errorHandler();
		        break;
		    }
		  };

		  xhr.onerror = function () {
		    console.error("The request couldn't be completed.");
		    errorHandler();
		  };

		  if (data === null) {
		    xhr.send();
		  } else {
		    xhr.setRequestHeader("Content-Type", "application/json;charset=utf-8");
		    xhr.send(data);
		  }
		}
	function listItems(items) {
		// Clear the current results
		var itemList = $('item-list');
		itemList.innerHTML = '';
        addFirstItem(itemList,items[0]);
        addSecondItem(itemList,items[1]);
        addThirdItem(itemList, items[2]);
        initMap(items[0].lat, items[0].lng, items[1].lat, items[1].lng, items[2].lat, items[2].lng);
	}	
	function addFirstItem(itemList, item) {
		// create the <li> tag and specify the id and class attributes
		var li = $('li', {
			className : 'firstResult'
		});
		// item image
		if (item.image_url) {
			li.appendChild($('img', {
				src : item.image_url
			}));
		} else {
			li.appendChild($('img', {
				src : 'https://www.bu.edu/riscs/files/2009/04/bu-campus.jpg'
			}))
		}
		// section
		var section = $('div', {});

		// title
		var title = $('a', {
			href : item.url,
			target : '_blank',
			className : 'item-name'
		});
		title.innerHTML = item.name;
		section.appendChild(title);

		// category
		var category = $('p', {
			className : 'item-category'
		});
		category.innerHTML = 'Category: ' + item.categories.join(', ');
		section.appendChild(category);

		var stars = $('div', {
			className : 'stars'
		});
		
		for (var i = 0; i < 3; i++) {
			var star = $('i', {
				className : 'fa fa-star'
			});
			stars.appendChild(star);
		}
		section.appendChild(stars);
		// address
		var address = $('a', {
			href:itemaddress.url
			className : 'item-address'
		});
		var addressHTML =  item.address;
		address.innerHTML = addressHTML;
        section.appendChild(address);
		li.appendChild(section);
		itemList.appendChild(li);
	}
	function addSecondItem(itemList, item) {
		// create the <li> tag and specify the id and class attributes
		var li = $('li', {
			className : 'secondResult'
		});
		// item image
		if (item.image_url) {
			li.appendChild($('img', {
				src : item.image_url
			}));
		} else {
			li.appendChild($('img', {
				src : 'https://www.bu.edu/riscs/files/2009/04/bu-campus.jpg'
			}))
		}
		// section
		var section = $('div', {});

		// title
		var title = $('a', {
			href : item.url,
			target : '_blank',
			className : 'item-name2'
		});
		title.innerHTML = item.name;
		section.appendChild(title);

		// category
		var category = $('p', {
			className : 'item-category2'
		});
		category.innerHTML = 'Category: ' + item.categories.join(', ');
		section.appendChild(category);

		var stars = $('div', {
			className : 'stars2'
		});
		
		for (var i = 0; i < 2; i++) {
			var star = $('i', {
				className : 'fa fa-star'
			});
			stars.appendChild(star);
		}
		section.appendChild(stars);
		// address
		var address = $('a', {
			href:itemaddress.url
			className : 'item-address2'
		});
		var addressHTML =  item.address;
		address.innerHTML = addressHTML;
        section.appendChild(address);
		li.appendChild(section);
		itemList.appendChild(li);
	}
	function addThirdItem(itemList, item) {
		// create the <li> tag and specify the id and class attributes
		var li = $('li', {
			className : 'thirdResult'
		});
		// item image
		if (item.image_url) {
			li.appendChild($('img', {
				src : item.image_url
			}));
		} else {
			li.appendChild($('img', {
				src : 'https://www.bu.edu/riscs/files/2009/04/bu-campus.jpg'
			}))
		}
		// section
		var section = $('div', {});

		// title
		var title = $('a', {
			href : item.url,
			target : '_blank',
			className : 'item-name3'
		});
		title.innerHTML = item.name;
		section.appendChild(title);

		// category
		var category = $('p', {
			className : 'item-category3'
		});
		category.innerHTML = 'Category: ' + item.categories.join(', ');
		section.appendChild(category);

		var stars = $('div', {
			className : 'stars3'
		});
		
			var star = $('i', {
				className : 'fa fa-star'
			});
			stars.appendChild(star);
		// address
		var address = $('p', {
			className : 'item-address3'
		});
		section.appendChild(stars);
		// address
		var address = $('a', {
			href:itemaddress.url
			className : 'item-address'
		});
		var addressHTML =  item.address;
		address.innerHTML = addressHTML;
        section.appendChild(address);
		li.appendChild(section);
		itemList.appendChild(li);
	}
	function loadMatchingResult() {
		console.log('loadMatchingResult');
		// The request parameters
		var url = './search';
		var img_src=$('myImg');
		var params = 'img_src=' +img_src.src ;
		var req = JSON.stringify({});

		// display loading message
		showLoadingMessage('Loading Matching Results...');

		// make AJAX call
		ajax('GET', url + '?' + params, req,
		// successful callback
		function(res) {
			var items = JSON.parse(res);
			if (!items || items.length === 0) {
				showWarningMessage('No matching result.');
			} else {
				listItems(items);
			}
		},
		// failed callback
		function() {
			showErrorMessage('Cannot load matching results.');
		});
	}
	function initMap(lat1,lng1, lat2,lng2, lat3, lng3) {
        var uluru = {lat: lat1, lng: lng1};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 15,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
        var uluru2 = {lat: lat2, lng: -lng2};
        var map2 = new google.maps.Map(document.getElementById('map2'), {
          zoom: 15,
          center: uluru2
        });
        var marker2 = new google.maps.Marker({
          position: uluru2,
          map: map2
        });
        var uluru3 = {lat: lat3, lng: lng3};
        var map3 = new google.maps.Map(document.getElementById('map3'), {
          zoom: 15,
          center: uluru3
        });
        var marker = new google.maps.Marker({
          position: uluru3,
          map: map3
        });
      }
	
})();
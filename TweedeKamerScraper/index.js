var Xray = require('x-ray');
var fs = require('fs');
var x = Xray();

var members = [];
var url = [];

x('https://www.tweedekamer.nl/kamerleden_en_commissies/alle_kamerleden', 'tbody', [{
	  naam: ['.goto-member@href'] 
}])(function(err, obj) {
	// console.log(obj[0].naam)
	url = obj[0].naam
})
	.then(getMembers)

function getMembers(){
	x('https://www.tweedekamer.nl/kamerleden_en_commissies/alle_kamerleden', '.member-detail-container', [{
		  naam: 'td .toggle-member-info',
		  roepnaam: 'td span',
		  fractie: 'td:nth-of-type(3) span',
		  woonplaats: 'td:nth-of-type(4) span',
		  leeftijd: 'td:nth-of-type(5) span .sort-value',
		  geslacht: 'td:nth-of-type(6) span',
		  ancinienniteit: 'td:nth-of-type(7) span'
	}])(function(err, obj) {
		obj.forEach(function(member, i) {
			// get date of birth from miliseconds
			member.leeftijd = parseInt(member.leeftijd) * 1000 + 86400000;
			member.leeftijd = new Date(member.leeftijd); 

			// add url
			member.url = url[i];
			getTwitter(member);
		});
	})
};	

function getTwitter (member){
	console.log('twitter');
	var link;
	x(member.url, 'section', [{
	  twitter: '.list-social .___twitter@href'
	}])(function(err, obj) {
		console.log(obj);
		link = obj[0].twitter;
		member.twitter = link;
	});
	members.push(member);
};


function writeFile () {
	console.log(members)
	fs.writeFile('leden.json', JSON.stringify(members), (err) => {
    if (err) throw err;
    console.log('The file has been saved!');
  })
}

setTimeout(function() {writeFile()}, 60000);



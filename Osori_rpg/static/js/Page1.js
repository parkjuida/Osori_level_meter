function Listplus() {
  var List_box = document.getElementById('level_meter_users');
  var li = document.createElement("li");
  li.addEventListener("click", function(){clickLists()}, false);
  var text = "이름";
  li.image.src="paper1.png";
}
Listplus();
function Levels(data) {
  var _exp = data.exp;
  var _commits = data.commit; //레포 커밋수
  var _visits = data.visits; // visit횟수
  var _parvisits = data.parvisits; // parvisit횟수
  var _ranks = data.ranks; // 동아리 운영 기여도
  var _login = data.login; // login 횟수
                           // "Boss : 회장", "VBoss : 부회장", "Some : 각종임원"


  _exp = _exp + _commits*10 + _visits*20 + _parvisits*50 + _login*10;

  if (_rank == "Boss")
    {exp += 4000;}
  else if (_rank == "VBoss")
    {exp += 2500;}
  else if (_rank == "Some")
    {exp += 1000;}

  if (_exp < 250)
    {data.level = 1;}
  else if (250 <= _exp && _exp < 950)
    {data.level = 2;}
  else if (950 <= _exp && _exp < 2450)
    {data.level = 3;}
  else if (2450 <= _exp && _exp < 5450)
    {data.level = 4;}
  else
    {data.level = 5;}

  data.exp = _exp;
}

function (){

}

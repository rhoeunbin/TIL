function test() {
    var p1 = document.getElementById('password').value;
    var p2 = document.getElementById('password_confirmation').value;
    
    if( p1.length < 8 ) {
            alert('8글자 이상 입력하라구');
            return false;
        }
        
        if( p1 != p2 ) {
          alert("틀렸어?대박");
          return false;
        } 
        else{
          alert("맞았어?좀 치네");
          return true;
        }
    }
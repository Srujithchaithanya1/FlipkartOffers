function myFun()
{
    var bank = $('#bank').val();
    var CD = $('#CD').val();
    var pg =$('#pg').val();
    var minp =$('#minp').val();
    var maxp = $('#maxp').val();
    $.ajax({
        url:"/join",
        type:"POST",
        data:{bank:bank,
                CD:CD,
                pg:pg ,
                minp:minp,
                maxp:maxp                  
            
            }
    }).done(function(response){
        var html="<table border='20' class='table-responsive'><tr><th>Product</th><th>Price</th><th>Offer</th><th>Link</th></tr>";
        response=response.result;
        
        $.each(response,function(key,val){
                for(let i=0;i<val.length;i++)
                {   
                    html+="<tr>"+"<td>"+val[i][0]+"</td>"+"<td>"+val[i][1]+"</td>"+"<td>"+val[i][2]+"</td>"+ "<td>"+"<a "+"href=" +val[i][3]+">"+"Link </a>"+"</td>"+    "</tr>";
                }
                // html+="<tr><td>"+val[1]+"</td></tr>";
            });
            html +="</table>";

            document.getElementById("mypage").innerHTML=html;
    });

    
    
};


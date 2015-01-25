

(function(){
    $('.form-signin').on({

        "submit":function(e){
            e.preventDefault();

           var data =  $(this).serialize();
            $.ajax({
                url:"/authenticate/",
                data:data,
                type:"POST",
                dataType:"json",
                success:function(data){
                    console.log(data);
                    if(data.success){
                        window.location = '/home';
                    }

                    if(data.error){
                        $('#error').html(data.error);
                    }
                }
            })
        }
    })
    $('.form-register').on({

        "submit":function(e){
            e.preventDefault();

           var data =  $(this).serialize();
            $.ajax({
                url:"/create/",
                data:data,
                type:"POST",
                dataType:"json",
                success:function(data){
                    console.log(data);
                    if(data.success){
                        window.location='/';
                    }
                    if(data.error){
                        $('#error').html(data.error);
                    }
                }
            })
        }
    })

})()
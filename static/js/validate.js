$(document).ready(()=>{
  Show();
});

const Show = ()=>{
    $("#form_index").submit((e)=>{
      e.preventDefault();
      value_income = parseInt($("#income").val());
      value_goal = parseInt($("#goal").val());
      value_month = parseInt($("#month").val());
      value_max = parseInt($("#max").val());
      value_bank = parseFloat($("#bank").val());
      console.log(value_income);
      console.log(value_goal);
      console.log(value_month);
      console.log(value_max);
      console.log(value_bank);
      let saving = (value_goal*value_bank/12) / (Math.pow((1+value_bank/12),value_month) - 1)
      console.log(saving);
      let htmlInsertWarning="";
      $("#show").empty();
      if (value_income < saving){
          htmlInsertWarning = `<font color="red" size="3">Nhập lỗi</font>`;
          document.querySelector("#show").insertAdjacentHTML('afterbegin', htmlInsertWarning);
      }
      else if (max > value_income){
        htmlInsertWarning = `<font color="red" size="3">Nhập lỗi</font>`;
        document.querySelector("#show").insertAdjacentHTML('afterbegin', htmlInsertWarning);
      }
      else {
        console.log("AAAAA");
        window.location = `../saving`;
      }
      return false;
    })

}

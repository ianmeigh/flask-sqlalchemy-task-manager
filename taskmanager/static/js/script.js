document.addEventListener('DOMContentLoaded', function () {
  M.Sidenav.init(document.querySelectorAll('.sidenav'), {});
  M.Modal.init(document.querySelectorAll('.modal'), {});

  M.Datepicker.init(document.querySelectorAll('.datepicker'), {
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year
    format: "dd mmmm, yyyy",
    i18n: { done: "Select" },
    autoClose: true
  });
  M.FormSelect.init(document.querySelectorAll('select'), {});
  M.Collapsible.init(document.querySelectorAll('.collapsible'), {});
});

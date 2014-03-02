var advisor = advisor || {};

$(function () {
  advisor.Programs = new advisor.ProgramCollection();
  var p = new advisor.Program({id: 3});
  advisor.Programs.reset([p]);
  (new advisor.ProgramCollectionView())
});

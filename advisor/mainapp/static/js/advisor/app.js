var advisor = advisor || {};


$(function () {
  traj = parseInt($('trajid').text()) || 1;
  advisor.Programs = new advisor.ProgramCollection();
  var p = new advisor.Program({id: 3});
  advisor.Programs.reset([p]);
  (new advisor.ProgramCollectionView())

  var t = new advisor.Trajectory({id: 1});
  t.fetch({
    success: function() {
      t.fetchRelated('semesters', {
        success: function() {
          advisor.Semesters = t.get('semesters');
          advisor.SemestersViews = new advisor.SemesterCollectionView();
        }
      });
    }
  });
});

$(document).ready(function() {
  $('#slide').click(function() {
    $('#semesters').slideToggle();
    //advisor.SemestersViews.addAll();
  })
})

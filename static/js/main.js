$(document).on('click', '.article', function(e) {
    $('.active').removeClass('active')
    e.preventDefault();
    var self = $(this);
    self.addClass('active');
    $('.more_details').load('/article/?slug='+self.data('slug'));
});

$(document).on('click', 'a.back-link', function(e) {
    e.preventDefault();
    window.history.back();
    return false;
});

$(document).on('click', '.date-filter', function(e) {
    e.preventDefault();
    var self = $(this);
    $('.more_list').load('/articlefilter/?date='+self.data('date'));
});

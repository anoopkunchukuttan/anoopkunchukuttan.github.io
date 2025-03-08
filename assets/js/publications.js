function filterList(keyword) {
    let items = document.querySelectorAll('.publication-item');
    let years = document.querySelectorAll('.year-header');
    let visibleYears = new Set();
    
    items.forEach(item => {
        let classes = item.className.split(" ");
        let keywordMatch = (keyword === 'all' || classes.includes(keyword.replace(" ", "_")));
        
        if (keywordMatch) {
            item.style.display = '';
            visibleYears.add(classes[classes.length - 1]); // Capture the year class
        } else {
            item.style.display = 'none';
        }
    });
    
    years.forEach(year => {
        let yearClass = year.classList[1];
        if (visibleYears.has(yearClass)) {
            year.style.display = '';
        } else {
            year.style.display = 'none';
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const reviewsContainer = document.querySelector('.banner4 .reviews-container');
    const leftArrow = document.querySelector('.banner4 .left-arrow');
    const rightArrow = document.querySelector('.banner4 .right-arrow');
  
    let scrollAmount = 0;
    const step = 300; // Adjust the scroll step as needed
  
    leftArrow.addEventListener('click', function() {
      console.log('Left arrow clicked');
      if (scrollAmount > 0) {
        scrollAmount = Math.max(scrollAmount - step, 0);
        reviewsContainer.style.transform = `translateX(-${scrollAmount}px)`;
      }
    });
  
    rightArrow.addEventListener('click', function() {
      console.log('Right arrow clicked');
      scrollAmount = Math.min(scrollAmount + step, reviewsContainer.scrollWidth - reviewsContainer.clientWidth);
      reviewsContainer.style.transform = `translateX(-${scrollAmount}px)`;
    });
  });
  document.addEventListener('DOMContentLoaded', function() {
    const questions = document.querySelectorAll('.banner6 .question');
  
    questions.forEach(function(question) {
      question.addEventListener('click', function() {
        const answer = this.nextElementSibling;
        if (answer.style.display === 'block') {
          answer.style.display = 'none';
        } else {
          answer.style.display = 'block';
        }
      });
    });
  });
  
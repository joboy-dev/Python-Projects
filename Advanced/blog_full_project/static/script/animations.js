var blogs = document.querySelectorAll('#blog-list .blog')

function animationOnScroll() {
    blogs.forEach((blog) => {
        blog.classList.add('blog-visible')
    })
}

window.addEventListener('load', animationOnScroll);
window.addEventListener('scroll', animationOnScroll);
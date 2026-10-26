// Header state, mobile menu and scroll reveal
const header = document.querySelector('.site-header');
const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 40);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

const btn = document.querySelector('.menu-btn');
const nav = document.querySelector('.nav');
btn.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  btn.classList.toggle('open', open);
  btn.textContent = open ? 'CLOSE' : 'MENU';
  document.body.style.overflow = open ? 'hidden' : '';
});

const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

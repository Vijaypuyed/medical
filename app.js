// app.js
const grid = document.getElementById('moviesGrid');
const modal = document.getElementById('movieModal');
const closeModal = document.getElementById('closeModal');
const modalPoster = document.getElementById('modalPoster');
const modalTitle = document.getElementById('modalTitle');
const modalMeta = document.getElementById('modalMeta');
const modalDesc = document.getElementById('modalDesc');
const trailerWrapper = document.getElementById('trailerWrapper');
const imdbLink = document.getElementById('imdbLink');
const bookBtn = document.getElementById('bookBtn');

function createCard(movie){
  const card = document.createElement('div');
  card.className = 'card';
  card.tabIndex = 0;

  const img = document.createElement('img');
  img.src = movie.poster;
  img.alt = movie.title;
  card.appendChild(img);

  const body = document.createElement('div');
  body.className = 'card-body';
  const title = document.createElement('h3');
  title.className = 'title';
  title.textContent = movie.title;
  body.appendChild(title);
  const year = document.createElement('div');
  year.className = 'year';
  year.textContent = `${movie.year} • ${movie.genre}`;
  body.appendChild(year);

  card.appendChild(body);

  card.addEventListener('click', () => openDetail(movie));
  return card;
}

function openDetail(movie){
  modalPoster.src = movie.poster;
  modalTitle.textContent = movie.title;
  modalMeta.textContent = `${movie.year} • ${movie.genre}`;
  modalDesc.textContent = movie.desc;
  imdbLink.href = movie.external || '#';
  // embed YouTube trailer (responsive)
  const vidId = parseYoutubeId(movie.trailer);
  if(vidId){
    trailerWrapper.innerHTML = `<iframe width="100%" height="100%" src="https://www.youtube.com/embed/${vidId}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
  } else {
    trailerWrapper.innerHTML = `<p style="padding:12px;color:#ddd">Trailer not available.</p>`;
  }
  modal.setAttribute('aria-hidden','false');
}

function parseYoutubeId(url){
  try{
    const u = new URL(url);
    if(u.hostname.includes('youtube.com')){
      return u.searchParams.get('v');
    }
    if(u.hostname === 'youtu.be'){
      return u.pathname.slice(1);
    }
  }catch(e){return null}
  return null;
}

closeModal.addEventListener('click', ()=> modal.setAttribute('aria-hidden','true'));
modal.addEventListener('click', (e)=> { if(e.target === modal) modal.setAttribute('aria-hidden','true') });
bookBtn.addEventListener('click', ()=> alert('Booking flow: this is a demo — implement payment & seat selection separately.'));

function init(){
  MOVIES.forEach(m => grid.appendChild(createCard(m)));
}
init();

/* 留福美装 クリニック清掃サイト 共通スクリプト
   イントロ演出・メニュー・スクロール表示は tomefuku.jp と同じ処理です。 */

// ---------- Intro splash screen(トップページのみ) / 下層ページのファーストビュー表示 ----------
(function(){
  const intro = document.getElementById('introScreen');
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const heroReveal = ['.hero-eyebrow','.hero h1','.hero-sub','.hero-actions','.scroll-cue'];
  function showHero(){
    heroReveal.forEach(sel => {
      const el = document.querySelector(sel);
      if (el) el.classList.add('is-visible');
    });
  }
  if (!intro) {
    // 下層ページ:イントロは出さず、ヒーローの文字だけ同じ動きで表示
    requestAnimationFrame(() => requestAnimationFrame(showHero));
    return;
  }
  function finishIntro(){
    intro.classList.add('intro-hide');
    document.body.style.overflow = '';
    showHero();
  }
  if (prefersReduced) {
    finishIntro();
  } else {
    document.body.style.overflow = 'hidden';
    const introTimer = setTimeout(finishIntro, 1600);
    intro.addEventListener('click', () => { clearTimeout(introTimer); finishIntro(); });
  }
})();

// ---------- Mobile menu ----------
(function(){
  const hbtn = document.getElementById('hamburgerBtn');
  const menu = document.getElementById('mobileMenu');
  const closeBtn = document.getElementById('mobileMenuClose');
  if (!hbtn || !menu) return;
  function openMenu(){
    menu.classList.add('open');
    hbtn.classList.add('is-open');
    hbtn.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }
  function closeMenu(){
    menu.classList.remove('open');
    hbtn.classList.remove('is-open');
    hbtn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
  hbtn.addEventListener('click', () => {
    menu.classList.contains('open') ? closeMenu() : openMenu();
  });
  closeBtn.addEventListener('click', closeMenu);
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
})();

// ---------- Scroll reveal ----------
(function(){
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('is-visible'));
  }
})();

// ---------- 施工事例タブ(カテゴリーで絞り込み) ----------
(function(){
  const tabs = document.querySelector('.works-tabs');
  if (!tabs) return;
  const cards = document.querySelectorAll('.works-grid .work-card');
  tabs.querySelectorAll('button').forEach(btn => {
    btn.setAttribute('type', 'button');
    btn.addEventListener('click', () => {
      tabs.querySelectorAll('button').forEach(b => { b.classList.remove('active'); b.setAttribute('aria-selected','false'); });
      btn.classList.add('active');
      btn.setAttribute('aria-selected','true');
      const cat = btn.dataset.cat || btn.textContent.trim();
      cards.forEach(card => {
        card.hidden = !(cat === 'すべて' || (card.dataset.cat || '').split(' ').indexOf(cat) !== -1);
      });
    });
  });
})();

// ---------- お問い合わせフォーム(Googleフォームへ送信) ----------
// 送信先・項目IDは tomefuku.jp と同じフォームです(通知メールの届け先も同じ)。
// 既存フォームの5項目に合わせ、クリニック用の追加項目は「お問い合わせ内容」にまとめて送ります。
(function(){
  var form = document.getElementById('contactForm');
  if(!form) return;
  var note = document.getElementById('cfNote');
  var GFORM_ACTION = 'https://docs.google.com/forms/d/e/1FAIpQLSch4809NCWThpmHUmwqbB1qrIv6VNFKfKgZHptj_A4yrY2xKg/formResponse';
  var ENTRY = {
    name: 'entry.2013235324',     // お名前 ← ご担当者名
    email: 'entry.1287921021',    // メールアドレス
    tel: 'entry.2080655205',      // 電話番号
    address: 'entry.1583159882',  // ご住所 ← 所在地
    message: 'entry.25669776'     // お問い合わせ内容 ← 医院名・清掃内容・頻度・本文をまとめて送信
  };
  var submitted = false;
  var iframe = document.getElementById('hidden_iframe');
  iframe.addEventListener('load', function(){
    if(!submitted) return; // ignore the initial blank load
    form.style.display = 'none';
    note.textContent = 'お問い合わせを受け付けました。内容を確認のうえ、折り返しご連絡いたします。';
    if (typeof window.gtag === 'function') { window.gtag('event', 'generate_lead', {form: 'clinic_contact'}); }
  });

  function val(n){ var el = form.elements[n]; return el ? String(el.value || '').trim() : ''; }

  form.addEventListener('submit', function(e){
    e.preventDefault();
    var clinic = val('clinic');
    var name = val('name');
    var email = val('email');
    var tel = val('tel');
    var address = val('address');
    var frequency = val('frequency');
    var body = val('message');
    var services = Array.prototype.map.call(
      form.querySelectorAll('input[name="service"]:checked'), function(c){ return c.value; }
    );

    var message =
      '【クリニック清掃サイトからのお問い合わせ】\n' +
      '医院・施設名:' + clinic + '\n' +
      '希望する清掃内容:' + (services.length ? services.join('、') : '未選択') + '\n' +
      '希望する清掃頻度:' + (frequency || '未選択') + '\n' +
      '----------\n' +
      (body || '(記入なし)') + '\n' +
      '----------\n' +
      '送信ページ:' + location.href;

    var params = new URLSearchParams();
    params.append(ENTRY.name, name);
    params.append(ENTRY.email, email);
    params.append(ENTRY.tel, tel);
    params.append(ENTRY.address, address);
    params.append(ENTRY.message, message);

    var tempForm = document.createElement('form');
    tempForm.action = GFORM_ACTION;
    tempForm.method = 'POST';
    tempForm.target = 'hidden_iframe';
    tempForm.style.display = 'none';
    params.forEach(function(value, key){
      var input = document.createElement('input');
      input.type = 'hidden';
      input.name = key;
      input.value = value;
      tempForm.appendChild(input);
    });
    document.body.appendChild(tempForm);
    submitted = true;
    tempForm.submit();
    document.body.removeChild(tempForm);
  });
})();

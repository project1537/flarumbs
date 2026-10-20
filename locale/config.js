// Bosanski (BS)

(function () {
  // Gramatička množina: 1, 21, 31… / 2–4, 22–24… / ostalo (5–20, 25–30…)
  function oblik(n) {
    var d = n % 10, s = n % 100;
    if (d === 1 && s !== 11) return 0;
    if (d >= 2 && d <= 4 && (s < 12 || s > 14)) return 1;
    return 2;
  }

  // [bez broja, 1·21, 2–4, 5+] za svaki padež:
  // nom = bez „za/prije“, gen = „prije …“, aku = „za …“
  var R = {
    m:  { nom: ['jedna minuta', 'minuta', 'minute', 'minuta'],
          gen: ['jedne minute', 'minute', 'minute', 'minuta'],
          aku: ['jednu minutu', 'minutu', 'minute', 'minuta'] },
    h:  { nom: ['jedan sat', 'sat', 'sata', 'sati'],
          gen: ['jednog sata', 'sata', 'sata', 'sati'],
          aku: ['jedan sat', 'sat', 'sata', 'sati'] },
    d:  { nom: ['jedan dan', 'dan', 'dana', 'dana'],
          gen: ['jednog dana', 'dana', 'dana', 'dana'],
          aku: ['jedan dan', 'dan', 'dana', 'dana'] },
    M:  { nom: ['jedan mjesec', 'mjesec', 'mjeseca', 'mjeseci'],
          gen: ['jednog mjeseca', 'mjeseca', 'mjeseca', 'mjeseci'],
          aku: ['jedan mjesec', 'mjesec', 'mjeseca', 'mjeseci'] },
    y:  { nom: ['jedna godina', 'godina', 'godine', 'godina'],
          gen: ['jedne godine', 'godine', 'godine', 'godina'],
          aku: ['jednu godinu', 'godinu', 'godine', 'godina'] }
  };

  function vrijeme(n, bezSufiksa, kljuc, buducnost) {
    var jedinica = R[kljuc.charAt(0) === 'M' ? 'M' : kljuc.charAt(0)];
    var padez = bezSufiksa ? 'nom' : (buducnost ? 'aku' : 'gen');
    if (kljuc.length === 1) return jedinica[padez][0];
    return n + ' ' + jedinica[padez][oblik(n) + 1];
  }

  // Nazivi mjeseci: genitiv uz dan („8. oktobra 2026.“), nominativ samostalno („oktobar 2026“)
  var mjeseciGen = 'januara_februara_marta_aprila_maja_juna_jula_augusta_septembra_oktobra_novembra_decembra'.split('_');
  var mjeseciNom = 'januar_februar_mart_april_maj_jun_jul_august_septembar_oktobar_novembar_decembar'.split('_');
  var UZ_DAN = /D[oD]?\.?(\[[^[\]]*\]|\s)+MMMM?/;
  function mjeseci(datum, format) {
    return UZ_DAN.test(format) ? mjeseciGen[datum.month()] : mjeseciNom[datum.month()];
  }
  mjeseci.s = mjeseciNom;
  mjeseci.f = mjeseciGen;

  dayjs.locale({
    name: 'bs',
    weekdays: 'nedjelja_ponedjeljak_utorak_srijeda_četvrtak_petak_subota'.split('_'),
    weekdaysShort: 'ned_pon_uto_sri_čet_pet_sub'.split('_'),
    weekdaysMin: 'ne_po_ut_sr_če_pe_su'.split('_'),
    months: mjeseci,
    monthsShort: 'jan_feb_mar_apr_maj_jun_jul_aug_sep_okt_nov_dec'.split('_'),
    weekStart: 1,
    yearStart: 4,
    formats: {
      LT: 'H:mm',
      LTS: 'H:mm:ss',
      L: 'D. M. YYYY.',
      LL: 'D. MMMM YYYY.',
      LLL: 'D. MMMM YYYY. [u] H:mm',
      LLLL: 'dddd, D. MMMM YYYY. [u] H:mm'
    },
    relativeTime: {
      future: 'za %s',
      past: 'prije %s',
      s: 'nekoliko sekundi',
      m: vrijeme, mm: vrijeme,
      h: vrijeme, hh: vrijeme,
      d: vrijeme, dd: vrijeme,
      M: vrijeme, MM: vrijeme,
      y: vrijeme, yy: vrijeme
    },
    ordinal: function (n) { return n + '.'; }
  });
})();

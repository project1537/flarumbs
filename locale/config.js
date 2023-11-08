// Bosanski (BS)

dayjs.locale({
  name: 'bs',
  weekdays: 'nedjelja_ponedjeljak_utorak_srijeda_četvrtak_petak_subota'.split('_'),
  weekdaysShort: 'ned_pon_uto_sri_čet_pet_sub'.split('_'),
  weekdaysMin: 'ne_po_ut_sr_če_pe_su'.split('_'),
  months: 'januar_februar_mart_april_maj_juni_juli_august_septembar_oktobar_novembar_decembar'.split('_'),
  monthsShort: 'jan_feb_mar_apr_maj_jun_jul_aug_sep_okt_nov_dec'.split('_'),
  weekStart: 1,
  formats: {
    LT: 'HH:mm',
    LTS: 'HH:mm:ss',
    L: 'DD.MM.YYYY',
    LL: 'D MMMM YYYY',
    LLL: 'D MMMM YYYY HH:mm',
    LLLL: 'dddd, D MMMM YYYY HH:mm'
	},
  relativeTime: {
    future: 'za %s',
    past: 'prije %s',
    s: 'par sekundi',
		m: 'jednu minutu',
		mm: '%d minuta',
		h: 'jedan sat',
		hh: '%d sati',
		d: 'jedan dan',
		dd: '%d dana',
		M: 'jedan mjesec',
		MM: '%d mjeseci',
		y: 'jednu godinu',
		yy: '%d godina'
  },
  ordinal: n => `${n}.`
}, null, false);

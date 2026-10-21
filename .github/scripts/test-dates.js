// Checks the dates and relative times that locale/config.js produces.
//
// Flarum exposes dayjs globally with the relativeTime and localizedFormat
// plugins and then runs locale/config.js, so this does the same.
//
//   npm install --no-save dayjs@1 && node .github/scripts/test-dates.js
const path = require('path');

global.dayjs = require('dayjs');
dayjs.extend(require('dayjs/plugin/relativeTime'));
dayjs.extend(require('dayjs/plugin/localizedFormat'));
require(path.join(__dirname, '..', '..', 'locale', 'config.js'));

const failures = [];
function expect(what, actual, wanted) {
  if (actual !== wanted) failures.push(`${what}: got "${actual}", expected "${wanted}"`);
}

if (dayjs.locale() !== 'bs') failures.push(`active locale is "${dayjs.locale()}", expected "bs"`);

// [amount, unit, past, future, without suffix]
const RELATIVE = [
  [10, 'second', 'prije nekoliko sekundi', 'za nekoliko sekundi', 'nekoliko sekundi'],
  [1, 'minute', 'prije jedne minute', 'za jednu minutu', 'jedna minuta'],
  [2, 'minute', 'prije 2 minute', 'za 2 minute', '2 minute'],
  [5, 'minute', 'prije 5 minuta', 'za 5 minuta', '5 minuta'],
  [11, 'minute', 'prije 11 minuta', 'za 11 minuta', '11 minuta'],
  [12, 'minute', 'prije 12 minuta', 'za 12 minuta', '12 minuta'],
  [21, 'minute', 'prije 21 minute', 'za 21 minutu', '21 minuta'],
  [22, 'minute', 'prije 22 minute', 'za 22 minute', '22 minute'],
  [1, 'hour', 'prije jednog sata', 'za jedan sat', 'jedan sat'],
  [2, 'hour', 'prije 2 sata', 'za 2 sata', '2 sata'],
  [5, 'hour', 'prije 5 sati', 'za 5 sati', '5 sati'],
  [21, 'hour', 'prije 21 sata', 'za 21 sat', '21 sat'],
  [1, 'day', 'prije jednog dana', 'za jedan dan', 'jedan dan'],
  [3, 'day', 'prije 3 dana', 'za 3 dana', '3 dana'],
  [21, 'day', 'prije 21 dana', 'za 21 dan', '21 dan'],
  [1, 'month', 'prije jednog mjeseca', 'za jedan mjesec', 'jedan mjesec'],
  [3, 'month', 'prije 3 mjeseca', 'za 3 mjeseca', '3 mjeseca'],
  [5, 'month', 'prije 5 mjeseci', 'za 5 mjeseci', '5 mjeseci'],
  [1, 'year', 'prije jedne godine', 'za jednu godinu', 'jedna godina'],
  [2, 'year', 'prije 2 godine', 'za 2 godine', '2 godine'],
  [5, 'year', 'prije 5 godina', 'za 5 godina', '5 godina'],
  [21, 'year', 'prije 21 godine', 'za 21 godinu', '21 godina'],
];

const now = dayjs('2026-10-21T12:00:00');
for (const [amount, unit, past, future, bare] of RELATIVE) {
  const label = `${amount} ${unit}`;
  expect(`${label} ago`, now.subtract(amount, unit).from(now), past);
  expect(`in ${label}`, now.add(amount, unit).from(now), future);
  expect(`${label} without suffix`, now.subtract(amount, unit).from(now, true), bare);
}

// Formats from core.lib.datetime_formats in locale/core.yml, and the
// localized formats Flarum uses through them.
const FORMATS = [
  ['2026-02-08T09:05:00', 'dddd, D. M. YYYY. [u] H:mm', 'nedjelja, 8. 2. 2026. u 9:05'],
  ['2026-02-08T09:05:00', 'D. MMM', '8. feb'],
  ['2026-02-08T09:05:00', 'll', '8. feb 2026.'],
  ['2026-02-08T09:05:00', 'MMMM YYYY', 'februar 2026'],
  ['2026-02-08T09:05:00', 'D. M. YYYY. [u] H:mm', '8. 2. 2026. u 9:05'],
  ['2026-02-08T09:05:00', 'L', '8. 2. 2026.'],
  ['2026-02-08T09:05:00', 'LL', '8. februara 2026.'],
  ['2026-02-08T09:05:00', 'LLL', '8. februara 2026. u 9:05'],
  ['2026-02-08T09:05:00', 'LLLL', 'nedjelja, 8. februara 2026. u 9:05'],
  ['2026-02-08T09:05:00', 'LT', '9:05'],
  ['2026-08-03T18:30:00', 'dddd, D. MMMM', 'ponedjeljak, 3. augusta'],
  ['2026-08-03T18:30:00', 'MMMM', 'august'],
  ['2026-05-21T00:00:00', 'dddd', 'četvrtak'],
];
for (const [date, format, wanted] of FORMATS) {
  expect(`${date} as "${format}"`, dayjs(date).format(format), wanted);
}

const total = RELATIVE.length * 3 + FORMATS.length;
if (failures.length) {
  console.error(failures.join('\n'));
  console.error(`${failures.length} of ${total} date checks failed`);
  process.exit(1);
}
console.log(`${total} date checks passed`);

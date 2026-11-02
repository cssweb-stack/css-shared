// Calendar dates are explicit ISO dates, never inferred or shifted by local time.
module.exports = function eventDate(value) {
  if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(value)) {
    throw new Error(`Event date must be an unambiguous YYYY-MM-DD value: ${value}`);
  }
  const date = new Date(`${value}T00:00:00Z`);
  if (!Number.isFinite(date.getTime()) || date.toISOString().slice(0, 10) !== value) {
    throw new Error(`Invalid event calendar date: ${value}`);
  }
  const options = { timeZone: 'UTC' };
  const month = date.toLocaleDateString('en-US', { ...options, month: 'short' }).toUpperCase();
  return {
    iso: value,
    compact: `${month} ${date.getUTCDate()}`,
    full: date.toLocaleDateString('en-US', {
      ...options, weekday: 'long', month: 'long', day: 'numeric', year: 'numeric'
    })
  };
};

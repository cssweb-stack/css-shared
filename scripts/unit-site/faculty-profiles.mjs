// One faculty record supplies both the directory card and individual bio sidebar.
export function resolveFacultyPerson(data) {
if (!data.personSlug) return undefined;
const records = Array.isArray(data.people) ? data.people : data.faculty;
const person = records?.find(record => record.slug === data.personSlug);
if (!person) throw new Error(`No faculty record found for profile: ${data.personSlug}`);
return person;
}

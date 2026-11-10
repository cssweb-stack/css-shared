// One faculty record supplies both the directory card and individual bio sidebar.
export function resolveFacultyPerson(data) {
if (!data.personSlug) return undefined;
const person = data.faculty?.find(record => record.slug === data.personSlug);
if (!person) throw new Error(`No faculty record found for profile: ${data.personSlug}`);
return person;
}

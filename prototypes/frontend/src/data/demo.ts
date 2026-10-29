// Ausschließlich synthetische Daten; kein offizieller Studien- oder Leistungsnachweis.
export const modules = [
  {
    id: 'math',
    code: 'MATH · 101',
    progress: 62,
    topics: 8,
    credits: 6,
    color: 'mint',
    icon: 'sigma',
  },
  {
    id: 'systems',
    code: 'CS · 204',
    progress: 38,
    topics: 6,
    credits: 5,
    color: 'lavender',
    icon: 'cpu',
  },
  {
    id: 'research',
    code: 'STUD · 110',
    progress: 24,
    topics: 5,
    credits: 3,
    color: 'sand',
    icon: 'book',
  },
] as const;
export type ModuleId = (typeof modules)[number]['id'];
export const documents = [
  {
    id: 'vectors',
    title: 'docVectors',
    module: 'math',
    type: 'pdf',
    pages: 18,
    date: '2026-10-21',
  },
  {
    id: 'processes',
    title: 'docProcesses',
    module: 'systems',
    type: 'pdf',
    pages: 12,
    date: '2026-10-20',
  },
  {
    id: 'sources',
    title: 'docSources',
    module: 'research',
    type: 'pdf',
    pages: 8,
    date: '2026-10-19',
  },
  { id: 'audio', title: 'docAudio', module: 'math', type: 'audio', pages: 0, date: '2026-10-18' },
] as const;
export type DemoDocument = (typeof documents)[number];
export type StudyEvent = {
  id: string;
  title: string;
  translated: boolean;
  module: ModuleId;
  date: string;
  time: string;
  kind: 'session' | 'event' | 'exam';
  local?: boolean;
};
export const initialEvents: StudyEvent[] = [
  {
    id: 'a',
    title: 'reviewSession',
    translated: true,
    module: 'math',
    date: '2026-10-22',
    time: '09:00',
    kind: 'session',
  },
  {
    id: 'b',
    title: 'systemsClass',
    translated: true,
    module: 'systems',
    date: '2026-10-22',
    time: '14:00',
    kind: 'event',
  },
  {
    id: 'c',
    title: 'researchSession',
    translated: true,
    module: 'research',
    date: '2026-10-23',
    time: '10:30',
    kind: 'session',
  },
];
export const noteData = [
  { id: 'math', title: 'noteVectors', body: 'noteBody', example: 'noteExample' },
  { id: 'systems', title: 'noteProcesses', body: 'noteSystemsBody', example: 'noteSystemsExample' },
  {
    id: 'research',
    title: 'noteResearch',
    body: 'noteResearchBody',
    example: 'noteResearchExample',
  },
] as const;

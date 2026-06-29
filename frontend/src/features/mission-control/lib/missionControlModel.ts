export type MissionControlStep = {
  id: string;
  label: string;
  status: "ready" | "waiting" | "running" | "done" | "blocked";
  detail: string;
};

export const missionControlSteps: MissionControlStep[] = [
  { id: "topic", label: "Sujet", status: "ready", detail: "Prêt" },
  { id: "research", label: "Recherche", status: "waiting", detail: "En attente" },
  { id: "script", label: "Script", status: "waiting", detail: "En attente" },
  { id: "voice", label: "Voix", status: "waiting", detail: "En attente" },
  { id: "visuals", label: "Visuels", status: "waiting", detail: "En attente" },
  { id: "edit", label: "Montage", status: "waiting", detail: "En attente" },
  { id: "approval", label: "Validation", status: "blocked", detail: "Contrôle humain" },
  { id: "publish", label: "Publication", status: "waiting", detail: "Privé par défaut" },
];

// frontend/src/app/player-summary/player-summary.interface.ts
export interface Shot {
    x: number;
    y: number;
}

export interface Game {
    date: string;
    shots: Shot[];
}

export interface PlayerSummary {
    player_name: string;
    team: string;
    games: Game[];
}
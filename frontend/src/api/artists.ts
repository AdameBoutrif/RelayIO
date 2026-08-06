import { apiFetch } from "./client";

import type { ArtistNames } from "../types/artist";

export function getArtists(): Promise<ArtistNames[]> {
    return apiFetch<ArtistNames[]>("/artists/");
}
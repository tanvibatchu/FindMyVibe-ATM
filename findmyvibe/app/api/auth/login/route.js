import { NextResponse } from "next/server";

export async function GET() {
const scopes = [
    "user-top-read",
    "user-read-recently-played",
    "playlist-read-private",
    "playlist-read-collaborative",
    "playlist-modify-public",
    "playlist-modify-private",
];

const params = new URLSearchParams({
    response_type: "code",
    client_id: process.env.SPOTIFY_CLIENT_ID,
    scope: scopes.join(" "),
    redirect_uri: process.env.SPOTIFY_REDIRECT_URI,
    show_dialog: "true",
});
const spotifyAuthUrl =
    `https://accounts.spotify.com/authorize?${params.toString()}`;

return NextResponse.redirect(spotifyAuthUrl);
}

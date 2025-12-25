import { NextResponse } from "next/server";

export async function GET(req) {
  // Parse the incoming request URL
const { searchParams } = new URL(req.url);

  // Spotify sends this ?code=XYZ
const code = searchParams.get("code");

  // This is enough for Spotify to accept the redirect
return NextResponse.json({
    success: true,
    message: "Spotify auth successful",
    code: code,
});
}

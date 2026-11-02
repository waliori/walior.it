// www goes to the apex; everything else is a static asset from site/ (_redirects and _headers apply there).
export default {
  fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname.startsWith('www.')) { url.hostname = url.hostname.slice(4); return Response.redirect(url.toString(), 301); }
    return env.ASSETS.fetch(request);
  },
};

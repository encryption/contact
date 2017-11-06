export default send => async (req, res) => {
  try {
    await send(req.body);
  } catch (e) {
    console.error(e);
  }

  let referer = req.get('Referer');
  if (referer) return res.redirect(referer);

  res.status(204).send();
};

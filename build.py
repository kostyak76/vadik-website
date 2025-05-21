# for more information, read https://staticjinja.readthedocs.io/en/latest/user/advanced.html

from uuid import uuid4
from staticjinja import Site
from staticjinja.reloader import Reloader


class CustomReloader(Reloader):

  def event_handler(self, *args, **kwargs):
    self.site.env.globals["randomHash"] = uuid4()
    super().event_handler(*args, **kwargs)


def main():
  site = Site.make_site(
    searchpath="src",
    outpath="build",
    # contexts=[(r".*\.md", md_context)],
    # rules=[(r".*\.md", render_md)],
    env_globals={"randomHash": uuid4()}
  )

  site.render()
  CustomReloader(site).watch()


if __name__ == '__main__':
  main()

from chroma_feedback import wording
from .api import get_api
from .group import get_groups, process_groups
from .light import get_lights, process_lights

args = None


def init(program):
	global args

	if not args:
		program.add_argument('--lifx-light-light', action = 'append')
		program.add_argument('--lifx-light-group', action = 'append')
	args = program.parse_known_args()[0]


def run(status):
	api = get_api()

	# use groups

	if args.lifx_light_group:
		groups = get_groups(args.lifx_light_group)

		if not groups:
			exit(wording.get('group_no') + wording.get('exclamation_mark'))
		return process_groups(status, groups)

	# use lights

	lights = get_lights(api.get_lights(), args.lifx_light_light)

	if not lights:
		exit(wording.get('light_no') + wording.get('exclamation_mark'))
	return process_lights(status, lights)

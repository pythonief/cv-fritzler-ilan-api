from operator import ge
from app.utils import create_json_response
from app.curriculum.models import Skill, SkillSchema
from app.curriculum.models import Language, LanguageSchema
from app.curriculum.models import Reference, ReferenceSchema
from flask import Blueprint, request
from flask_login import login_required
# Views

curriculum = Blueprint('curriculum', __name__, url_prefix='/api')

# MarshMallow Schemas
skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)
language_schema = LanguageSchema()
languages_schema = LanguageSchema(many=True)
reference_schema = ReferenceSchema()
references_schema = ReferenceSchema(many=True)


@curriculum.route('/info', methods=['GET'])
def get_info():
    info = {
        'fullname': 'Ilan Emanuel Fritzler',
        'short_description': 'Jr Backend Development in Python',
        'contact': {
            'address': 'Strobel 4051, Mar del Plata, Argentina',
            'email': 'fritzlerilan@gmail.com',
            'phone': '+542236690789',
        },
        'born': {
            'in': 'Mar del Plata, Buenos Aires, Argentina',
            'dob': '15 June 1994',
        },
        'nationality': 'Argentinian',
        'about': 'Passionate student of Programming with a special interest in ' +
        'the back-end stack. I want to get surrounded for new technologies to ' +
        'improve my skills. I’ve achieved knowledge of Python in the last 6 months.'
    }
    return create_json_response('Success', 200, personal_information=info)


"""
    Skills Views
"""


@curriculum.route('/skills', methods=['GET'])
def get_skills():
    global skills_schema

    skills = Skill.query.all()
    output = skills_schema.dump(skills)

    return create_json_response('Success', 200, skills=output)


@curriculum.route('/skills/<int:id>', methods=['GET'])
def get_skill(id):
    global skill_schema
    try:
        skill = Skill.query.filter_by(id=id).first()
        if skill:
            output = skill_schema.dump(skill)
            return create_json_response('Found', 200, skill=output)
        return create_json_response('', 404)
    except Exception as e:
        return create_json_response('Error', 404, error=e)


@curriculum.route('/skills/add', methods=['POST'])
@login_required
def set_skill():
    global skill_schema

    name = request.form.get('name', None)
    description = request.form.get('description', None)
    valid_skill, list_error = Skill.create_skill(name, description)

    if not valid_skill:
        return create_json_response('Bad request', 400, errors=list_error)

    valid_skill.save()
    skill = skill_schema.dump(valid_skill)
    return create_json_response('Success', 201, skill=skill)


@curriculum.route('/skills/<int:id>', methods=['PUT'])
@login_required
def update_skill(id):
    global skill_schema
    try:
        skill = Skill.query.filter_by(id=id).first()
        if skill:
            skill.name = request.form.get('name', skill.name)
            skill.description = request.form.get(
                'description', skill.description)

            skill.save()
            output = skill_schema.dump(skill)
            return create_json_response('Updated', 200, skill=output)
        return create_json_response('Not Found', 404)
    except Exception as e:
        return create_json_response('Error', 404, error=e)


@curriculum.route('/skills/<int:id>', methods=['DELETE'])
@login_required
def delete_skill(id):
    global skill_schema
    try:
        skill = Skill.query.filter_by(id=id).first()
        if skill:
            skill.delete()
            output = skill_schema.dump(skill)
            return create_json_response('Deleted', 200, skill=output)
        return create_json_response('', 404)
    except Exception as e:
        return create_json_response('Error', 404, error=e)


"""
    Language Views
"""


@curriculum.route('/langs', methods=['GET'])
def get_langs():
    global language_schema

    langs = Language.query.all()
    output = languages_schema.dump(langs)

    return create_json_response('Success', 200, langs=output)


""" 
Busca un idioma por nombre o por id 
"""


@curriculum.route('/langs/<lang>', methods=['GET'])
def get_one_lang(lang):
    global language_schema
    try:
        int(lang)
        language = Language.query.filter_by(id=lang).first()
    except Exception:
        language = Language.query.filter_by(name=lang).first()

    if language:
        output = language_schema.dump(language)
        return create_json_response('Found', 200, language=output)
    return create_json_response('', 404)


@curriculum.route('langs/add', methods=['POST'])
@login_required
def add_lang():
    global language_schema

    name = request.form.get('name', None)
    description = request.form.get('description', None)

    new_language, errors = Language.create_lang(name, description)

    if not errors:
        new_language.save()
        output = language_schema.dump(new_language)
        return create_json_response('Success', 201, created=output)
    return create_json_response('Fields Missing', 400, errors=errors)


@curriculum.route('langs/<lang>', methods=['PUT'])
@login_required
def update_lang(lang):
    global language_schema
    try:
        int(lang)
        language = Language.query.filter_by(id=lang).first()
    except Exception as e:
        language = Language.query.filter_by(name=lang).first()
    if not language:
        return create_json_response('', 404)

    language.name = request.form.get('name', language.name)
    language.description = request.form.get(
        'description', language.description)
    language.save()
    output = language_schema.dump(language)
    return create_json_response('Updated', 200, updated=output)


@curriculum.route('langs/<lang>', methods=['DELETE'])
@login_required
def delete_lang(lang):
    global language_schema
    try:
        int(lang)
        language = Language.query.filter_by(id=lang).first()
    except Exception as e:
        language = Language.query.filter_by(name=lang).first()
    if not language:
        return create_json_response('', 404)
    language.delete()
    output = language_schema.dump(language)
    return create_json_response('Deleted', 200, deleted=output)


"""
    Reference Views
"""


@curriculum.route('/refs', methods=['GET'])
def get_refs():
    global references_schema

    refs = Reference.query.all()
    output = languages_schema.dump(refs)

    return create_json_response('Success', 200, refs=output)


@curriculum.route('/refs/<id>', methods=['GET'])
def get_ref(id):
    global reference_schema
    try:
        ref = Reference.query.filter_by(id=id).first()
        if ref:
            output = reference_schema.dump(ref)
            return create_json_response('Found', 200, ref=output)
        return create_json_response('', 404)
    except Exception as e:
        return create_json_response('Error', 404, error=e)


@curriculum.route('refs/add', methods=['POST'])
@login_required
def add_reference():
    global reference_schema

    name = request.form.get('name', None)
    description = request.form.get('description', None)
    company = request.form.get('company', None)
    email = request.form.get('email', None)

    new_ref, errors = Language.create_lang(name, email, company, description)

    if not errors:
        new_ref.save()
        output = reference_schema.dump(new_ref)
        return create_json_response('Success', 201, created=output)
    return create_json_response('Fields Missing', 400, errors=errors)


@curriculum.route('refs/<lang>', methods=['PUT'])
@login_required
def update_lang(id):
    global reference_schema
    ref = Reference.query.filter_by(id=id).first()

    if not ref:
        return create_json_response('', 404)

    ref.name = request.form.get('name', ref.name)
    ref.email = request.form.get('email', ref.email)
    ref.company = request.form.get('company', ref.company)
    ref.description = request.form.get('description', ref.description)
    ref.save()
    output = reference_schema.dump(ref)
    return create_json_response('Updated', 200, updated=output)


@curriculum.route('/refs/<id>', methods=['DELETE'])
def delete_ref(id):
    global reference_schema
    try:
        ref = Reference.query.filter_by(id=id).first()
        if ref:
            ref.delete()
            output = reference_schema.dump(ref)
            return create_json_response('Deleted', 200, ref=output)
        return create_json_response('', 404)
    except Exception as e:
        return create_json_response('Error', 404, error=e)

"""

"""
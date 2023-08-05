import abc
import sys

# compatible with Python 2 *and* 3:
ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()})


class AbstractAlephMarcReader(ABC):

    class Correspondent(ABC):
        """
        Represents an abstract correspondent.
        Both Persons and Organisations can be Correspondents.
        :param str|False name: the name of the correspondent, if any.
        :param str|False gnd: the GND of the correspondent, otherwise 'no_GND', if any.
        :param str|False roles: the role of the correspondent (author etc.), if any.

        """

        CORRESPONDENT_TYPE_PERSON = 'Person'
        CORRESPONDENT_TYPE_ORGANISATION = 'Organisation'

        def __init__(self, name, gnd, roles):
            self.name = name
            self.gnd = gnd
            self.roles = roles

        @abc.abstractmethod
        def get_type(self):
            """
            Gives the type of Correspondent.
            :return str: Type of correspondent, either 'person' or 'organisation'.
            """
            pass

    class Person(Correspondent):
        """
        Represents a person.
        :param str|False name: the name of the person (family name, first name), if any.
        :param str|False lifespan: the lifespan of the person (year of birth and death separated by a '-'), if any.
        :param str|False gnd: the GND of the person, otherwise 'no_GND', if any.
        :param str|False roles: the role of the person (author etc.), if any.

        """

        def __init__(self, name, lifespan, gnd, roles):
            super(AbstractAlephMarcReader.Person, self).__init__(name, gnd, roles)
            self.lifespan = lifespan

        def get_type(self):
            return AbstractAlephMarcReader.Correspondent.CORRESPONDENT_TYPE_PERSON

    class Organisation(Correspondent):
        """
        Represents a person.
        :param str|False name: the name of the person (family name, first name), if any.
        :param str|False gnd: the GND of the person, otherwise 'no_GND', if any.
        :param str|False roles: the role of the person (author etc.), if any.
        :param str|False place the place of the organisation.
        :param str|False division of the organisation.
        """

        def __init__(self, name, gnd, roles, place, division):
            super(AbstractAlephMarcReader.Organisation, self).__init__(name, gnd, roles)
            self.place = place
            self.division = division

        def get_type(self):
            return AbstractAlephMarcReader.Correspondent.CORRESPONDENT_TYPE_ORGANISATION

    class Place:
        """
        Represents a place.
        :param str|False name: the name of the place, if any.
        :param str|False gnd: the GND of the place, otherwise 'no_GND', if any.
        """

        def __init__(self, name, gnd):
            self.name = name
            self.gnd = gnd

    class Shelfmark:
        """
        Represents a shelfmark.
        :param str|False institution: the name of the institution, if any.
        :param str|False identifier: the identifier, if any.
        :param str|False country: the country, if any.
        :param str|False collection: the collection, if any.
        """
        def __init__(self, institution, identifier, country, collection):
            self.institution = institution
            self.identifier = identifier
            self.country = country
            self.collection = collection

    class Description:
        """
        Represents the physical description.
        :param str extent: the extent of the manuscript, i.e. number of pages.
        :param str|False attribute: the attribute of the manuscript, if any.
        :param str|False dimension: the dimension of the manuscript, if any.
        :param str|False supplement: supplementary material, if any.
        """
        def __init__(self, extent, attribute, dimension, supplement):
            self.extent = extent
            self.attribute = attribute
            self.dimension = dimension
            self.supplement = supplement

    class OriginalDate:
        """
        Represents the date, as written on the letter.
        :param str|False date; transcription of the date, as given in the letter, if any.
        :param str|False place; transcription of the place, as given in the letter, if any.
        """
        def __init__(self, date, place):
            self.date = date
            self.place = place

    class BiblioReference:
        """
        Represents bibliographic references.
        :param str reference; a string refering to one or more bibliographic items
        :param str|False prefix; prefix to the bibliographic item, if any. (e.g. "Abgedruckt in", "Inhaltsangabe", etc)
        """
        def __init__(self, reference, prefix):
            self.reference = reference
            self.prefix = prefix

        def get_pretty_string(self):
            """
            Returns a string combining prefix (if existing) and reference, separated by ': '
            :return: String combining prefix and reference
            """
            if self.prefix:
                return u'{}: {}'.format(self.prefix, self.reference)
            else:
                return self.reference

    class StandardizedDate:

        TIMESPAN_SEPARATOR_KNORA = u':'
        CALENDAR_PREFIX_KNORA = u'GREGORIAN' + TIMESPAN_SEPARATOR_KNORA
        TIMESPAN_SEPARATOR_ISO8601 = u'--'

        """
        Represents a standardized date.
        
        Can return a string representation following the KNORA date format as well as a representation following
        ISO 8601. Can hold both single dates and time intervals, both can be more or less precise.
        (Gregorian Calendar is always implied.)
        
        KNORA date format:
        `year[-month[-day]][:endYear[-endMonth[-endDay]]` (e.g. `1705-09-21` or `1705-09-23:1705-09-29`)
        
        The following ISO 8601 format is used:
        `year[-month[-day]][--endYear[-endMonth[-endDay]]` (e.g. `1705-09-21` or `1705-09-23--1705-09-29`)
        Intervals are always given with start and end date, not with duration.
        As separator of intervals, double hyphen is used instead of solidus (dash), to allow for use in file names etc.
        Dates are referred to by month, not by week.
        No exact time (below "day").
        Extended, not basic format is used for readability (e.g. `1705-09-21` not `17050921`)
        (See: https://en.wikipedia.org/wiki/ISO_8601)
        
        :param str start_span: If the date is precise, this represents the date;
        if the date is a time span, this represents the start of the time span.
        :param str|False end_span: if the date is precise, this must be False;
        else, this represents the end of the time span.
        """
        def __init__(self, start_span, end_span):
            self.start_span = start_span
            self.end_span = end_span
            self.__replace_separators()

        def get_standardized_date_string_KNORA(self):
            """
            Returns a string representation of the standardized date, following the KNORA internal standard.
            :return str:
            """
            res = self.CALENDAR_PREFIX_KNORA + self.start_span
            if self.end_span:
                res = res + self.TIMESPAN_SEPARATOR_KNORA + self.end_span
            return res

        def get_standardized_date_string_ISO8601(self):
            """
            Returns a string representation of the standardized date, following ISO 8601.
            :return str:
            """
            res = self.start_span
            if self.end_span:
                res = res + self.TIMESPAN_SEPARATOR_ISO8601 + self.end_span
            return res

        def __replace_separators(self):
            self.start_span = self.start_span.replace('.', '-')
            if self.end_span:
                self.end_span = self.end_span.replace('.', '-')


    def __init__(self, gnd_index, file_path):
        """
        :param gnd_index: index of the GND subfield.
        """
        self._gnd_index = gnd_index
        self._file_path = file_path

    @abc.abstractmethod
    def __get_subfield_texts(self, marc_field, index):
        pass

    @abc.abstractmethod
    def __get_field(self, index):
        pass

    def _handle_subfields_cardinality_max_one(self, subfields, field_tag, subfield_code):
        """
        Handles subfields whose occurrence is max one (optional):
        - empty list -> False
        - one entry -> str
        If more than one Subfield should occur, the first one is used and a warning printed to `stderr`.
        :param [str] subfields: the subfields to handle
        :param str field_tag: The marc field tag of the field containing subfields
        :param str subfield_code: The marc subfield code of subfields
        :return: False | str
        """
        if len(subfields) == 1:
            return subfields[0]
        elif len(subfields) > 1:
            sys.stderr.write(u'!!! WARNING: In \'{}\', Field \'{}\', Subfield \'{}\': '
                             u'Expected maximum 1 Subfield, found {}.\n'
                             .format(self._file_path, field_tag, subfield_code, len(subfields)))
            return subfields[0]
        else:
            return False

    def _get_person_info(self, marc_field, field_tag):
        """
        Extracts person information from a Marc field incl. the GND, if any.
        :param pymarc.field.Field marc_field: the Marc21 field that contains information about a person.
        :param str field_tag: The marc field tag of marc_field
        :return: Person
        """

        name = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(marc_field, 'a'), field_tag, 'a')

        date = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(marc_field, 'd'), field_tag, 'd')

        gnd = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(marc_field, self._gnd_index),
                                                         field_tag, self._gnd_index)
        if gnd:
            gnd = gnd.replace(',', '') # get rid of trailing comma

        # get rid of trailing comma in roles
        roles = list(map(lambda role: role.replace(',', ''), self.__get_subfield_texts(marc_field, '4')))

        return self.Person(name, date, gnd, roles)

    def _get_organisation_info(self, marc_field, field_tag):
        """
        Extracts organisation info from a Marc field incl. the GND, if any.
        :param pymarc.field.Field marc_field: the Marc21 field that contains information about a person.
        :param str field_tag: The marc field tag of marc_field
        :return: [Organisation]
        """
        name = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(marc_field, 'a'), field_tag, 'a')

        gnd = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(marc_field, self._gnd_index),
                                                         field_tag, self._gnd_index)
        if gnd:
            gnd = gnd.replace(',', '')  # get rid of trailing comma

        # get rid of trailing comma in roles
        roles = list(map(lambda role: role.replace(',', ''), self.__get_subfield_texts(marc_field, '4')))

        place = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(marc_field, 'g'), field_tag, 'g')

        division = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(marc_field, 'b'), field_tag, 'b')

        return self.Organisation(name, gnd, roles, place, division)

    def get_author(self):
        """
        Returns information about the author.
        :return: [Correspondent]
        """
        author = []
        for field in self.__get_field('100'):
            author.append(self._get_person_info(field, '100'))

        # check for recipients (700) that are actually authors
        for field in self.__get_field('700'):
            person = self._get_person_info(field, '700')

            if "aut" in person.roles:
                author.append(person)

        # check for recipient organisations (710) that are actually authors
        for field in self.__get_field('710'):
            organisation = self._get_organisation_info(field, '710')

            if "aut" in organisation.roles:
                author.append(organisation)

        return author
    get_author.__annotations__ = {'return': [Correspondent]}

    def get_recipient(self):
        """
        Returns information about the recipient.
        :return: [Correspondent]
        """
        recipient = []
        for field in self.__get_field('700'):
            person = self._get_person_info(field, '700')

            if "rcp" in person.roles:
                recipient.append(person)

        for field in self.__get_field('710'):
            organisation = self._get_organisation_info(field, '710')

            if "rcp" in organisation.roles:
                recipient.append(organisation)

        return recipient
    get_recipient.__annotations__ = {'return': [Correspondent]}

    def get_mentioned_person(self):
        """
        Returns information about a mentioned person.
        :return: [Person]
        """
        mentioned = []
        for field in self.__get_field('600'):
            mentioned.append(self._get_person_info(field, '600'))

        return mentioned
    get_mentioned_person.__annotations__ = {'return': [Person]}

    def get_standardized_date(self):
        """
        Returns the standardized date.
        :return: [StandardizedDate]
        """
        std_date = []
        for field in self.__get_field('046'):
            date_start = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'c'), '046', 'c')
            date_end = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'e'), '046', 'e')

            if date_start:
                date = self.StandardizedDate(date_start, date_end)
                std_date.append(date)

        return std_date
    get_standardized_date.__annotations__ = {'return': [StandardizedDate]}

    def get_date(self):
        """
        Returns the date.
        :return: [str]
        """
        date = []
        for field in self.__get_field('046'):
            date_text = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'c'), '046', 'c')

            if date_text:
                date.append(date_text)

        return date
    get_date.__annotations__ = {'return': [str]}

    def get_creation_place(self):
        """
        Returns the place of creation.
        :return: [Place]
        """
        creation_place = []

        for field in self.__get_field('751'):
            name = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'a'), '751', 'a')

            gnd = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, self._gnd_index), '751',
                                                             self._gnd_index)

            cp = self.Place(name, gnd)
            creation_place.append(cp)

        return creation_place
    get_creation_place.__annotations__ = {'return': [Place]}

    def get_shelfmark(self):
        """
        Returns the shelfmark.
        :return: [Shelfmark]
        """
        shelfmark = []

        for field in self.__get_field('852'):
            institution = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'a'), '852', 'a')
            identifier = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'p'), '852', 'p')
            country = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'n'), '852', 'n')
            collection = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'b'), '852', 'b')

            sm = self.Shelfmark(institution, identifier, country, collection)
            shelfmark.append(sm)

        return shelfmark
    get_shelfmark.__annotations__ = {'return': [Shelfmark]}

    def get_general_remarks(self):
        """
        Returns the general remarks.
        :return: [str]
        """
        footnote = []

        for field in self.__get_field('500'):
            footnote_text = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'a'), '500', 'a')

            if footnote_text:
                footnote.append(footnote_text)

        return footnote
    get_general_remarks.__annotations__ = {'return': [str]}

    def get_content_summary(self):
        """
        Returns the content summary.
        :return: [str]
        """
        summary = []

        for field in self.__get_field('520'):
            footnote_text = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'a'), '520', 'a')

            if footnote_text:
                summary.append(footnote_text)

        return summary
    get_content_summary.__annotations__ = {'return': [str]}

    def get_emanuscripta_doi(self):
        """
        Returns the emanuscripta DOI.
        :return: [str]
        """
        external_link = []

        for field in self.__get_field('024'):
            ext_link = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'a'), '024', 'a')

            if ext_link:
                external_link.append(ext_link)

        return external_link

    get_emanuscripta_doi.__annotations__ = {'return': [str]}

    def get_physical_description(self):
        """
        Returns the physical description.
        :return: [Description]
        """
        physical_description = []

        for field in self.__get_field('300'):
            extent = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'a'), '300', 'a')
            attribute = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'b'), '300', 'b')
            dimension = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'c'), '300', 'c')
            supplement = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'e'), '300', 'e')

            physical_description.append(self.Description(extent, attribute, dimension, supplement))

        return physical_description

    get_physical_description.__annotations__ = {'return': [Description]}

    def get_language(self):
        """
        Returns the language.
        :return: [str]
        """
        language = []

        for field in self.__get_field('041'):
            # subfield may occur several times
            lang = self.__get_subfield_texts(field, 'a')

            for lan in lang:
                language.append(lan)

        return language

    get_language.__annotations__ = {'return': [str]}

    def get_mentioned_organisation(self):
        """
        Returns the mentioned organisation.
        :return: [Organisation]
        """
        mentioned_organisation = []
        for field in self.__get_field('610'):
            mentioned_organisation.append(self._get_organisation_info(field, '610'))

        return mentioned_organisation

    get_mentioned_organisation.__annotations__ = {'return': [Organisation]}

    def get_supplement_remarks(self):
        """
        Returns comments on supplementing material following the letter.
        :return: [str]
        """
        remarks = []

        for field in self.__get_field('525'):
            footnote_text = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'a'), '525', 'a')

            if footnote_text:
                remarks.append(footnote_text)

        return remarks

    get_supplement_remarks.__annotations__ = {'return': [str]}

    def get_document_state(self):
        """
        Returns a description of the document state. (i.e. "original", "copy", "draft", etc.)
        :return: [str]
        """
        states = []

        for field in self.__get_field('250'):
            document_state = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'a'), '250', 'a')

            if document_state:
                states.append(document_state)

        return states

    get_document_state.__annotations__ = {'return': [str]}

    def get_original_date_and_place(self):
        """
        Returns a transcription of the date and place, as given on the letter.
        Conjectured information (starting with '[') is ignored.
        :return: [OriginalDate]
        """
        original_dates = []

        for field in self.__get_field('264'):
            date = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'c'), '264', 'c')
            place = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'a'), '264', 'a')

            if date and date.startswith('['):
                date = False
            if place and place.startswith('['):
                place = False

            if not (date or place):
                continue

            orig_date = self.OriginalDate(date, place)
            original_dates.append(orig_date)

        return original_dates

    get_original_date_and_place.__annotations__ = {'return': [OriginalDate]}

    def get_references_to_related_entries(self):
        """
        Returns a list of related entries.
        That is usually the case, if there are several document stages of the same letter.
        (E.g. Original, draft, copy, etc.)
        :return: [str]
        """
        references = []

        for field in self.__get_field('533'):
            ref = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'a'), '533', 'a')
            if ref:
                references.append(ref)

            ref = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'n'), '533', 'n')
            if ref:
                references.append(ref)

        for field in self.__get_field('534'):
            ref = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'n'), '534', 'n')
            if ref:
                references.append(ref)

        for field in self.__get_field('544'):
            ref = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'n'), '544', 'n')
            if ref:
                references.append(ref)

        return references

    get_references_to_related_entries.__annotations__ = {'return': [OriginalDate]}

    def get_bibliographic_references(self):
        """
        Returns bibliographic references relevant to the letter. (Usually, where it has been printed.)
        :return: [BiblioReference]
        """
        references = []

        for field in self.__get_field('581'):
            prefix = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'i'), '581', 'i')
            reference = self._handle_subfields_cardinality_max_one(self.__get_subfield_texts(field, 'a'), '581', 'a')
            biblio_ref = self.BiblioReference(reference, prefix)
            references.append(biblio_ref)

        return references

    get_bibliographic_references.__annotations__ = {'return': [BiblioReference]}






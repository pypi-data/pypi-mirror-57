"Main interface for polly service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_polly.client as client_scope

# pylint: disable=import-self
import mypy_boto3_polly.paginator as paginator_scope
from mypy_boto3_polly.type_defs import (
    ClientDescribeVoicesResponseTypeDef,
    ClientGetLexiconResponseTypeDef,
    ClientGetSpeechSynthesisTaskResponseTypeDef,
    ClientListLexiconsResponseTypeDef,
    ClientListSpeechSynthesisTasksResponseTypeDef,
    ClientStartSpeechSynthesisTaskResponseTypeDef,
    ClientSynthesizeSpeechResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_lexicon(self, Name: str) -> Dict[str, Any]:
        """
        Deletes the specified pronunciation lexicon stored in an AWS Region. A lexicon which has
        been deleted is not available for speech synthesis, nor is it possible to retrieve it using
        either the ``GetLexicon`` or ``ListLexicon`` APIs.

        For more information, see `Managing Lexicons
        <https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/DeleteLexicon>`_

        **Request Syntax**
        ::

          response = client.delete_lexicon(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the lexicon to delete. Must be an existing lexicon in the region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_voices(
        self,
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        IncludeAdditionalLanguageCodes: bool = None,
        NextToken: str = None,
    ) -> ClientDescribeVoicesResponseTypeDef:
        """
        Returns the list of voices that are available for use when requesting speech synthesis. Each
        voice speaks a specified language, is either male or female, and is identified by an ID,
        which is the ASCII version of the voice name.

        When synthesizing speech ( ``SynthesizeSpeech`` ), you provide the voice ID for the voice
        you want from the list of voices returned by ``DescribeVoices`` .

        For example, you want your news reader application to read news in a specific language, but
        giving a user the option to choose the voice. Using the ``DescribeVoices`` operation you can
        provide the user with a list of available voices to select from.

        You can optionally specify a language code to filter the available voices. For example, if
        you specify ``en-US`` , the operation returns a list of all available US English voices.

        This operation requires permissions to perform the ``polly:DescribeVoices`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/DescribeVoices>`_

        **Request Syntax**
        ::

          response = client.describe_voices(
              Engine='standard'|'neural',
              LanguageCode=
                  'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'
                  |'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'
                  |'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
              IncludeAdditionalLanguageCodes=True|False,
              NextToken='string'
          )
        :type Engine: string
        :param Engine:

          Specifies the engine (``standard`` or ``neural`` ) used by Amazon Polly when processing
          input text for speech synthesis.

        :type LanguageCode: string
        :param LanguageCode:

          The language identification tag (ISO 639 code for the language name-ISO 3166 country code)
          for filtering the list of voices returned. If you don't specify this optional parameter,
          all available voices are returned.

        :type IncludeAdditionalLanguageCodes: boolean
        :param IncludeAdditionalLanguageCodes:

          Boolean value indicating whether to return any bilingual voices that use the specified
          language as an additional language. For instance, if you request all languages that use US
          English (es-US), and there is an Italian voice that speaks both Italian (it-IT) and US
          English, that voice will be included if you specify ``yes`` but not if you specify ``no``
          .

        :type NextToken: string
        :param NextToken:

          An opaque pagination token returned from the previous ``DescribeVoices`` operation. If
          present, this indicates where to continue the listing.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Voices': [
                    {
                        'Gender': 'Female'|'Male',
                        'Id':
                        'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'
                        |'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'
                        |'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'
                        |'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'
                        |'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'
                        |'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'
                        |'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'
                        |'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'
                        |'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
                        'LanguageCode':
                        'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'
                        |'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'
                        |'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'
                        |'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'
                        |'tr-TR',
                        'LanguageName': 'string',
                        'Name': 'string',
                        'AdditionalLanguageCodes': [
                            'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'
                            |'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'
                            |'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'
                            |'ru-RU'|'sv-SE'|'tr-TR',
                        ],
                        'SupportedEngines': [
                            'standard'|'neural',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Voices** *(list) --*

              A list of voices with their properties.

              - *(dict) --*

                Description of the voice.

                - **Gender** *(string) --*

                  Gender of the voice.

                - **Id** *(string) --*

                  Amazon Polly assigned voice ID. This is the ID that you specify when calling the
                  ``SynthesizeSpeech`` operation.

                - **LanguageCode** *(string) --*

                  Language code of the voice.

                - **LanguageName** *(string) --*

                  Human readable name of the language in English.

                - **Name** *(string) --*

                  Name of the voice (for example, Salli, Kendra, etc.). This provides a human
                  readable voice name that you might display in your application.

                - **AdditionalLanguageCodes** *(list) --*

                  Additional codes for languages available for the specified voice in addition to
                  its default language.

                  For example, the default language for Aditi is Indian English (en-IN) because it
                  was first used for that language. Since Aditi is bilingual and fluent in both
                  Indian English and Hindi, this parameter would show the code ``hi-IN`` .

                  - *(string) --*

                - **SupportedEngines** *(list) --*

                  Specifies which engines (``standard`` or ``neural`` ) that are supported by a
                  given voice.

                  - *(string) --*

            - **NextToken** *(string) --*

              The pagination token to use in the next request to continue the listing of voices.
              ``NextToken`` is returned only if the response is truncated.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_lexicon(self, Name: str) -> ClientGetLexiconResponseTypeDef:
        """
        Returns the content of the specified pronunciation lexicon stored in an AWS Region. For more
        information, see `Managing Lexicons
        <https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/GetLexicon>`_

        **Request Syntax**
        ::

          response = client.get_lexicon(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the lexicon.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Lexicon': {
                    'Content': 'string',
                    'Name': 'string'
                },
                'LexiconAttributes': {
                    'Alphabet': 'string',
                    'LanguageCode':
                    'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'
                    |'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'
                    |'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'
                    |'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                    'LastModified': datetime(2015, 1, 1),
                    'LexiconArn': 'string',
                    'LexemesCount': 123,
                    'Size': 123
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Lexicon** *(dict) --*

              Lexicon object that provides name and the string content of the lexicon.

              - **Content** *(string) --*

                Lexicon content in string format. The content of a lexicon must be in PLS format.

              - **Name** *(string) --*

                Name of the lexicon.

            - **LexiconAttributes** *(dict) --*

              Metadata of the lexicon, including phonetic alphabetic used, language code, lexicon
              ARN, number of lexemes defined in the lexicon, and size of lexicon in bytes.

              - **Alphabet** *(string) --*

                Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .

              - **LanguageCode** *(string) --*

                Language code that the lexicon applies to. A lexicon with a language code such as
                "en" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so
                on.

              - **LastModified** *(datetime) --*

                Date lexicon was last modified (a timestamp value).

              - **LexiconArn** *(string) --*

                Amazon Resource Name (ARN) of the lexicon.

              - **LexemesCount** *(integer) --*

                Number of lexemes in the lexicon.

              - **Size** *(integer) --*

                Total size of the lexicon, in characters.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_speech_synthesis_task(self, TaskId: str) -> ClientGetSpeechSynthesisTaskResponseTypeDef:
        """
        Retrieves a specific SpeechSynthesisTask object based on its TaskID. This object contains
        information about the given speech synthesis task, including the status of the task, and a
        link to the S3 bucket containing the output of the task.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/GetSpeechSynthesisTask>`_

        **Request Syntax**
        ::

          response = client.get_speech_synthesis_task(
              TaskId='string'
          )
        :type TaskId: string
        :param TaskId: **[REQUIRED]**

          The Amazon Polly generated identifier for a speech synthesis task.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SynthesisTask': {
                    'Engine': 'standard'|'neural',
                    'TaskId': 'string',
                    'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
                    'TaskStatusReason': 'string',
                    'OutputUri': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'RequestCharacters': 123,
                    'SnsTopicArn': 'string',
                    'LexiconNames': [
                        'string',
                    ],
                    'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
                    'SampleRate': 'string',
                    'SpeechMarkTypes': [
                        'sentence'|'ssml'|'viseme'|'word',
                    ],
                    'TextType': 'ssml'|'text',
                    'VoiceId':
                    'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'
                    |'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'
                    |'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'
                    |'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'
                    |'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'
                    |'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'
                    |'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'
                    |'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
                    'LanguageCode':
                    'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'
                    |'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'
                    |'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'
                    |'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **SynthesisTask** *(dict) --*

              SynthesisTask object that provides information from the requested task, including
              output format, creation time, task status, and so on.

              - **Engine** *(string) --*

                Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when
                processing input text for speech synthesis. Using a voice that is not supported for
                the engine selected will result in an error.

              - **TaskId** *(string) --*

                The Amazon Polly generated identifier for a speech synthesis task.

              - **TaskStatus** *(string) --*

                Current status of the individual speech synthesis task.

              - **TaskStatusReason** *(string) --*

                Reason for the current status of a specific speech synthesis task, including errors
                if the task has failed.

              - **OutputUri** *(string) --*

                Pathway for the output speech file.

              - **CreationTime** *(datetime) --*

                Timestamp for the time the synthesis task was started.

              - **RequestCharacters** *(integer) --*

                Number of billable characters synthesized.

              - **SnsTopicArn** *(string) --*

                ARN for the SNS topic optionally used for providing status notification for a speech
                synthesis task.

              - **LexiconNames** *(list) --*

                List of one or more pronunciation lexicon names you want the service to apply during
                synthesis. Lexicons are applied only if the language of the lexicon is the same as
                the language of the voice.

                - *(string) --*

              - **OutputFormat** *(string) --*

                The format in which the returned output will be encoded. For audio stream, this will
                be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

              - **SampleRate** *(string) --*

                The audio frequency specified in Hz.

                The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000".
                The default value for standard voices is "22050". The default value for neural
                voices is "24000".

                Valid values for pcm are "8000" and "16000" The default value is "16000".

              - **SpeechMarkTypes** *(list) --*

                The type of speech marks returned for the input text.

                - *(string) --*

              - **TextType** *(string) --*

                Specifies whether the input text is plain text or SSML. The default value is plain
                text.

              - **VoiceId** *(string) --*

                Voice ID to use for the synthesis.

              - **LanguageCode** *(string) --*

                Optional language code for a synthesis task. This is only necessary if using a
                bilingual voice, such as Aditi, which can be used for either Indian English (en-IN)
                or Hindi (hi-IN).

                If a bilingual voice is used and no language code is specified, Amazon Polly will
                use the default language of the bilingual voice. The default language for any voice
                is the one returned by the `DescribeVoices
                <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation
                for the ``LanguageCode`` parameter. For example, if no language code is specified,
                Aditi will use Indian English rather than Hindi.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_lexicons(self, NextToken: str = None) -> ClientListLexiconsResponseTypeDef:
        """
        Returns a list of pronunciation lexicons stored in an AWS Region. For more information, see
        `Managing Lexicons <https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/ListLexicons>`_

        **Request Syntax**
        ::

          response = client.list_lexicons(
              NextToken='string'
          )
        :type NextToken: string
        :param NextToken:

          An opaque pagination token returned from previous ``ListLexicons`` operation. If present,
          indicates where to continue the list of lexicons.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Lexicons': [
                    {
                        'Name': 'string',
                        'Attributes': {
                            'Alphabet': 'string',
                            'LanguageCode':
                            'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'
                            |'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'
                            |'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'
                            |'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'
                            |'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                            'LastModified': datetime(2015, 1, 1),
                            'LexiconArn': 'string',
                            'LexemesCount': 123,
                            'Size': 123
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Lexicons** *(list) --*

              A list of lexicon names and attributes.

              - *(dict) --*

                Describes the content of the lexicon.

                - **Name** *(string) --*

                  Name of the lexicon.

                - **Attributes** *(dict) --*

                  Provides lexicon metadata.

                  - **Alphabet** *(string) --*

                    Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa``
                    .

                  - **LanguageCode** *(string) --*

                    Language code that the lexicon applies to. A lexicon with a language code such
                    as "en" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS,
                    and so on.

                  - **LastModified** *(datetime) --*

                    Date lexicon was last modified (a timestamp value).

                  - **LexiconArn** *(string) --*

                    Amazon Resource Name (ARN) of the lexicon.

                  - **LexemesCount** *(integer) --*

                    Number of lexemes in the lexicon.

                  - **Size** *(integer) --*

                    Total size of the lexicon, in characters.

            - **NextToken** *(string) --*

              The pagination token to use in the next request to continue the listing of lexicons.
              ``NextToken`` is returned only if the response is truncated.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_speech_synthesis_tasks(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Status: Literal["scheduled", "inProgress", "completed", "failed"] = None,
    ) -> ClientListSpeechSynthesisTasksResponseTypeDef:
        """
        Returns a list of SpeechSynthesisTask objects ordered by their creation date. This operation
        can filter the tasks by their status, for example, allowing users to list only tasks that
        are completed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/ListSpeechSynthesisTasks>`_

        **Request Syntax**
        ::

          response = client.list_speech_synthesis_tasks(
              MaxResults=123,
              NextToken='string',
              Status='scheduled'|'inProgress'|'completed'|'failed'
          )
        :type MaxResults: integer
        :param MaxResults:

          Maximum number of speech synthesis tasks returned in a List operation.

        :type NextToken: string
        :param NextToken:

          The pagination token to use in the next request to continue the listing of speech
          synthesis tasks.

        :type Status: string
        :param Status:

          Status of the speech synthesis tasks returned in a List operation

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'SynthesisTasks': [
                    {
                        'Engine': 'standard'|'neural',
                        'TaskId': 'string',
                        'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
                        'TaskStatusReason': 'string',
                        'OutputUri': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'RequestCharacters': 123,
                        'SnsTopicArn': 'string',
                        'LexiconNames': [
                            'string',
                        ],
                        'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
                        'SampleRate': 'string',
                        'SpeechMarkTypes': [
                            'sentence'|'ssml'|'viseme'|'word',
                        ],
                        'TextType': 'ssml'|'text',
                        'VoiceId':
                        'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'
                        |'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'
                        |'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'
                        |'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'
                        |'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'
                        |'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'
                        |'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'
                        |'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'
                        |'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
                        'LanguageCode':
                        'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'
                        |'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'
                        |'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'
                        |'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'
                        |'tr-TR'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              An opaque pagination token returned from the previous List operation in this request.
              If present, this indicates where to continue the listing.

            - **SynthesisTasks** *(list) --*

              List of SynthesisTask objects that provides information from the specified task in the
              list request, including output format, creation time, task status, and so on.

              - *(dict) --*

                SynthesisTask object that provides information about a speech synthesis task.

                - **Engine** *(string) --*

                  Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when
                  processing input text for speech synthesis. Using a voice that is not supported
                  for the engine selected will result in an error.

                - **TaskId** *(string) --*

                  The Amazon Polly generated identifier for a speech synthesis task.

                - **TaskStatus** *(string) --*

                  Current status of the individual speech synthesis task.

                - **TaskStatusReason** *(string) --*

                  Reason for the current status of a specific speech synthesis task, including
                  errors if the task has failed.

                - **OutputUri** *(string) --*

                  Pathway for the output speech file.

                - **CreationTime** *(datetime) --*

                  Timestamp for the time the synthesis task was started.

                - **RequestCharacters** *(integer) --*

                  Number of billable characters synthesized.

                - **SnsTopicArn** *(string) --*

                  ARN for the SNS topic optionally used for providing status notification for a
                  speech synthesis task.

                - **LexiconNames** *(list) --*

                  List of one or more pronunciation lexicon names you want the service to apply
                  during synthesis. Lexicons are applied only if the language of the lexicon is the
                  same as the language of the voice.

                  - *(string) --*

                - **OutputFormat** *(string) --*

                  The format in which the returned output will be encoded. For audio stream, this
                  will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

                - **SampleRate** *(string) --*

                  The audio frequency specified in Hz.

                  The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000".
                  The default value for standard voices is "22050". The default value for neural
                  voices is "24000".

                  Valid values for pcm are "8000" and "16000" The default value is "16000".

                - **SpeechMarkTypes** *(list) --*

                  The type of speech marks returned for the input text.

                  - *(string) --*

                - **TextType** *(string) --*

                  Specifies whether the input text is plain text or SSML. The default value is plain
                  text.

                - **VoiceId** *(string) --*

                  Voice ID to use for the synthesis.

                - **LanguageCode** *(string) --*

                  Optional language code for a synthesis task. This is only necessary if using a
                  bilingual voice, such as Aditi, which can be used for either Indian English
                  (en-IN) or Hindi (hi-IN).

                  If a bilingual voice is used and no language code is specified, Amazon Polly will
                  use the default language of the bilingual voice. The default language for any
                  voice is the one returned by the `DescribeVoices
                  <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation
                  for the ``LanguageCode`` parameter. For example, if no language code is specified,
                  Aditi will use Indian English rather than Hindi.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_lexicon(self, Name: str, Content: str) -> Dict[str, Any]:
        """
        Stores a pronunciation lexicon in an AWS Region. If a lexicon with the same name already
        exists in the region, it is overwritten by the new lexicon. Lexicon operations have eventual
        consistency, therefore, it might take some time before the lexicon is available to the
        SynthesizeSpeech operation.

        For more information, see `Managing Lexicons
        <https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/PutLexicon>`_

        **Request Syntax**
        ::

          response = client.put_lexicon(
              Name='string',
              Content='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}.
          That is, the name is a case-sensitive alphanumeric string up to 20 characters long.

        :type Content: string
        :param Content: **[REQUIRED]**

          Content of the PLS lexicon as string data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_speech_synthesis_task(
        self,
        OutputFormat: Literal["json", "mp3", "ogg_vorbis", "pcm"],
        OutputS3BucketName: str,
        Text: str,
        VoiceId: Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        LexiconNames: List[str] = None,
        OutputS3KeyPrefix: str = None,
        SampleRate: str = None,
        SnsTopicArn: str = None,
        SpeechMarkTypes: List[Literal["sentence", "ssml", "viseme", "word"]] = None,
        TextType: Literal["ssml", "text"] = None,
    ) -> ClientStartSpeechSynthesisTaskResponseTypeDef:
        """
        Allows the creation of an asynchronous synthesis task, by starting a new
        ``SpeechSynthesisTask`` . This operation requires all the standard information needed for
        speech synthesis, plus the name of an Amazon S3 bucket for the service to store the output
        of the synthesis task and two optional parameters (OutputS3KeyPrefix and SnsTopicArn). Once
        the synthesis task is created, this operation will return a SpeechSynthesisTask object,
        which will include an identifier of this task as well as the current status.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/StartSpeechSynthesisTask>`_

        **Request Syntax**
        ::

          response = client.start_speech_synthesis_task(
              Engine='standard'|'neural',
              LanguageCode=
                  'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'
                  |'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'
                  |'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
              LexiconNames=[
                  'string',
              ],
              OutputFormat='json'|'mp3'|'ogg_vorbis'|'pcm',
              OutputS3BucketName='string',
              OutputS3KeyPrefix='string',
              SampleRate='string',
              SnsTopicArn='string',
              SpeechMarkTypes=[
                  'sentence'|'ssml'|'viseme'|'word',
              ],
              Text='string',
              TextType='ssml'|'text',
              VoiceId=
                  'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'
                  |'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'
                  |'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'
                  |'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'
                  |'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'
                  |'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'
                  |'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu'
          )
        :type Engine: string
        :param Engine:

          Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when processing
          input text for speech synthesis. Using a voice that is not supported for the engine
          selected will result in an error.

        :type LanguageCode: string
        :param LanguageCode:

          Optional language code for the Speech Synthesis request. This is only necessary if using a
          bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or
          Hindi (hi-IN).

          If a bilingual voice is used and no language code is specified, Amazon Polly will use the
          default language of the bilingual voice. The default language for any voice is the one
          returned by the `DescribeVoices
          <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for the
          ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will use
          Indian English rather than Hindi.

        :type LexiconNames: list
        :param LexiconNames:

          List of one or more pronunciation lexicon names you want the service to apply during
          synthesis. Lexicons are applied only if the language of the lexicon is the same as the
          language of the voice.

          - *(string) --*

        :type OutputFormat: string
        :param OutputFormat: **[REQUIRED]**

          The format in which the returned output will be encoded. For audio stream, this will be
          mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

        :type OutputS3BucketName: string
        :param OutputS3BucketName: **[REQUIRED]**

          Amazon S3 bucket name to which the output file will be saved.

        :type OutputS3KeyPrefix: string
        :param OutputS3KeyPrefix:

          The Amazon S3 key prefix for the output speech file.

        :type SampleRate: string
        :param SampleRate:

          The audio frequency specified in Hz.

          The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The
          default value for standard voices is "22050". The default value for neural voices is
          "24000".

          Valid values for pcm are "8000" and "16000" The default value is "16000".

        :type SnsTopicArn: string
        :param SnsTopicArn:

          ARN for the SNS topic optionally used for providing status notification for a speech
          synthesis task.

        :type SpeechMarkTypes: list
        :param SpeechMarkTypes:

          The type of speech marks returned for the input text.

          - *(string) --*

        :type Text: string
        :param Text: **[REQUIRED]**

          The input text to synthesize. If you specify ssml as the TextType, follow the SSML format
          for the input text.

        :type TextType: string
        :param TextType:

          Specifies whether the input text is plain text or SSML. The default value is plain text.

        :type VoiceId: string
        :param VoiceId: **[REQUIRED]**

          Voice ID to use for the synthesis.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SynthesisTask': {
                    'Engine': 'standard'|'neural',
                    'TaskId': 'string',
                    'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
                    'TaskStatusReason': 'string',
                    'OutputUri': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'RequestCharacters': 123,
                    'SnsTopicArn': 'string',
                    'LexiconNames': [
                        'string',
                    ],
                    'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
                    'SampleRate': 'string',
                    'SpeechMarkTypes': [
                        'sentence'|'ssml'|'viseme'|'word',
                    ],
                    'TextType': 'ssml'|'text',
                    'VoiceId':
                    'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'
                    |'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'
                    |'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'
                    |'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'
                    |'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'
                    |'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'
                    |'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'
                    |'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
                    'LanguageCode':
                    'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'
                    |'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'
                    |'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'
                    |'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **SynthesisTask** *(dict) --*

              SynthesisTask object that provides information and attributes about a newly submitted
              speech synthesis task.

              - **Engine** *(string) --*

                Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when
                processing input text for speech synthesis. Using a voice that is not supported for
                the engine selected will result in an error.

              - **TaskId** *(string) --*

                The Amazon Polly generated identifier for a speech synthesis task.

              - **TaskStatus** *(string) --*

                Current status of the individual speech synthesis task.

              - **TaskStatusReason** *(string) --*

                Reason for the current status of a specific speech synthesis task, including errors
                if the task has failed.

              - **OutputUri** *(string) --*

                Pathway for the output speech file.

              - **CreationTime** *(datetime) --*

                Timestamp for the time the synthesis task was started.

              - **RequestCharacters** *(integer) --*

                Number of billable characters synthesized.

              - **SnsTopicArn** *(string) --*

                ARN for the SNS topic optionally used for providing status notification for a speech
                synthesis task.

              - **LexiconNames** *(list) --*

                List of one or more pronunciation lexicon names you want the service to apply during
                synthesis. Lexicons are applied only if the language of the lexicon is the same as
                the language of the voice.

                - *(string) --*

              - **OutputFormat** *(string) --*

                The format in which the returned output will be encoded. For audio stream, this will
                be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

              - **SampleRate** *(string) --*

                The audio frequency specified in Hz.

                The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000".
                The default value for standard voices is "22050". The default value for neural
                voices is "24000".

                Valid values for pcm are "8000" and "16000" The default value is "16000".

              - **SpeechMarkTypes** *(list) --*

                The type of speech marks returned for the input text.

                - *(string) --*

              - **TextType** *(string) --*

                Specifies whether the input text is plain text or SSML. The default value is plain
                text.

              - **VoiceId** *(string) --*

                Voice ID to use for the synthesis.

              - **LanguageCode** *(string) --*

                Optional language code for a synthesis task. This is only necessary if using a
                bilingual voice, such as Aditi, which can be used for either Indian English (en-IN)
                or Hindi (hi-IN).

                If a bilingual voice is used and no language code is specified, Amazon Polly will
                use the default language of the bilingual voice. The default language for any voice
                is the one returned by the `DescribeVoices
                <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation
                for the ``LanguageCode`` parameter. For example, if no language code is specified,
                Aditi will use Indian English rather than Hindi.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def synthesize_speech(
        self,
        OutputFormat: Literal["json", "mp3", "ogg_vorbis", "pcm"],
        Text: str,
        VoiceId: Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        LexiconNames: List[str] = None,
        SampleRate: str = None,
        SpeechMarkTypes: List[Literal["sentence", "ssml", "viseme", "word"]] = None,
        TextType: Literal["ssml", "text"] = None,
    ) -> ClientSynthesizeSpeechResponseTypeDef:
        """
        Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input must be valid,
        well-formed SSML. Some alphabets might not be available with all the voices (for example,
        Cyrillic might not be read at all by English voices) unless phoneme mapping is used. For
        more information, see `How it Works
        <https://docs.aws.amazon.com/polly/latest/dg/how-text-to-speech-works.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/SynthesizeSpeech>`_

        **Request Syntax**
        ::

          response = client.synthesize_speech(
              Engine='standard'|'neural',
              LanguageCode=
                  'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'
                  |'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'
                  |'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
              LexiconNames=[
                  'string',
              ],
              OutputFormat='json'|'mp3'|'ogg_vorbis'|'pcm',
              SampleRate='string',
              SpeechMarkTypes=[
                  'sentence'|'ssml'|'viseme'|'word',
              ],
              Text='string',
              TextType='ssml'|'text',
              VoiceId=
                  'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'
                  |'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'
                  |'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'
                  |'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'
                  |'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'
                  |'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'
                  |'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu'
          )
        :type Engine: string
        :param Engine:

          Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when processing
          input text for speech synthesis. Using a voice that is not supported for the engine
          selected will result in an error.

        :type LanguageCode: string
        :param LanguageCode:

          Optional language code for the Synthesize Speech request. This is only necessary if using
          a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or
          Hindi (hi-IN).

          If a bilingual voice is used and no language code is specified, Amazon Polly will use the
          default language of the bilingual voice. The default language for any voice is the one
          returned by the `DescribeVoices
          <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for the
          ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will use
          Indian English rather than Hindi.

        :type LexiconNames: list
        :param LexiconNames:

          List of one or more pronunciation lexicon names you want the service to apply during
          synthesis. Lexicons are applied only if the language of the lexicon is the same as the
          language of the voice. For information about storing lexicons, see `PutLexicon
          <https://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html>`__ .

          - *(string) --*

        :type OutputFormat: string
        :param OutputFormat: **[REQUIRED]**

          The format in which the returned output will be encoded. For audio stream, this will be
          mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

          When pcm is used, the content returned is audio/pcm in a signed 16-bit, 1 channel (mono),
          little-endian format.

        :type SampleRate: string
        :param SampleRate:

          The audio frequency specified in Hz.

          The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The
          default value for standard voices is "22050". The default value for neural voices is
          "24000".

          Valid values for pcm are "8000" and "16000" The default value is "16000".

        :type SpeechMarkTypes: list
        :param SpeechMarkTypes:

          The type of speech marks returned for the input text.

          - *(string) --*

        :type Text: string
        :param Text: **[REQUIRED]**

          Input text to synthesize. If you specify ``ssml`` as the ``TextType`` , follow the SSML
          format for the input text.

        :type TextType: string
        :param TextType:

          Specifies whether the input text is plain text or SSML. The default value is plain text.
          For more information, see `Using SSML
          <https://docs.aws.amazon.com/polly/latest/dg/ssml.html>`__ .

        :type VoiceId: string
        :param VoiceId: **[REQUIRED]**

          Voice ID to use for the synthesis. You can get a list of available voice IDs by calling
          the `DescribeVoices
          <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AudioStream': StreamingBody(),
                'ContentType': 'string',
                'RequestCharacters': 123
            }
          **Response Structure**

          - *(dict) --*

            - **AudioStream** (:class:`.StreamingBody`) --

              Stream containing the synthesized speech.

            - **ContentType** *(string) --*

              Specifies the type audio stream. This should reflect the ``OutputFormat`` parameter in
              your request.

              * If you request ``mp3`` as the ``OutputFormat`` , the ``ContentType`` returned is
              audio/mpeg.

              * If you request ``ogg_vorbis`` as the ``OutputFormat`` , the ``ContentType`` returned
              is audio/ogg.

              * If you request ``pcm`` as the ``OutputFormat`` , the ``ContentType`` returned is
              audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.

              * If you request ``json`` as the ``OutputFormat`` , the ``ContentType`` returned is
              audio/json.

            - **RequestCharacters** *(integer) --*

              Number of characters synthesized.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_voices"]
    ) -> paginator_scope.DescribeVoicesPaginator:
        """
        Get Paginator for `describe_voices` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_lexicons"]
    ) -> paginator_scope.ListLexiconsPaginator:
        """
        Get Paginator for `list_lexicons` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_speech_synthesis_tasks"]
    ) -> paginator_scope.ListSpeechSynthesisTasksPaginator:
        """
        Get Paginator for `list_speech_synthesis_tasks` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """


class Exceptions:
    ClientError: Boto3ClientError
    EngineNotSupportedException: Boto3ClientError
    InvalidLexiconException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidS3BucketException: Boto3ClientError
    InvalidS3KeyException: Boto3ClientError
    InvalidSampleRateException: Boto3ClientError
    InvalidSnsTopicArnException: Boto3ClientError
    InvalidSsmlException: Boto3ClientError
    InvalidTaskIdException: Boto3ClientError
    LanguageNotSupportedException: Boto3ClientError
    LexiconNotFoundException: Boto3ClientError
    LexiconSizeExceededException: Boto3ClientError
    MarksNotSupportedForFormatException: Boto3ClientError
    MaxLexemeLengthExceededException: Boto3ClientError
    MaxLexiconsNumberExceededException: Boto3ClientError
    ServiceFailureException: Boto3ClientError
    SsmlMarksNotSupportedForTextTypeException: Boto3ClientError
    SynthesisTaskNotFoundException: Boto3ClientError
    TextLengthExceededException: Boto3ClientError
    UnsupportedPlsAlphabetException: Boto3ClientError
    UnsupportedPlsLanguageException: Boto3ClientError

"""
Copyright (c) 2018 Stefan Stojanovic

"""

import numpy as np
from scipy.stats import norm
import warnings
from proteinko.schemas import get_schema, list_schema_names


class Proteinko:

    def _normalize(self, array, norm_range=(-1,1)):
        """
        Normalize range of values.
        :param array: 1d array of values.
        :param norm_range: range
        :return: 1d array
        """
        x = norm_range[0]
        y = norm_range[1]
        array = np.array(array)
        array = (array - min(array)) / (max(array) - min(array))
        return array * (np.abs(x - y)) + min([x, y])

    def _standardize(self, array):
        """
        Standardize range of values: z = (X-mu)/sigma
        :param array: 1d array
        :return: 1d array
        """
        array = (array - np.mean(array)) / np.std(array)
        return array

    def _prepare_schema(self, schema, normalize=False, standardize=False,
                        norm_range=(-1,1)):
        """
        Prepare schema for processing with get_signal function.
        :param schema: Initialized pd DataFrame with schema
        :return: Processed pd DataFrame
        """
        schema['amino_acid'] = schema['amino_acid'].str.upper()
        if normalize:
            schema['value'] = self._normalize(
                schema['value'], norm_range=norm_range
            )
        if standardize:
            schema['value'] = self._standardize(schema['value'])
        return schema

    def _model_dist(self, sequence, schema, sigma=0.8, vlen=100, trim=False,
                    normed=False):
        """
        Model distribution of properties specified in schema for given sequence.
        :param sequence: protein sequence
        :param schema: pandas dataframe with "amino_acid" and "value columns"
        :param sigma: sigma used for modeling individual amino acid residues
        :param vlen: return vector length
        :param trim: trim flanking slices of return vector
        :param normed: return vector is normalized to range [0,1]
        :return: 1d array
        """
        sequence = sequence.upper()
        S = np.zeros(100 * len(sequence) + 200)
        for i, amino_acid in enumerate(sequence):
            row = schema[schema['amino_acid'] == amino_acid]
            if len(row) != 1:
                warnings.warn(
                    'Ambiguous schema for amino acid {}. Value '
                    'will be set to mean value.'.format(amino_acid),
                    Warning
                )
                row_value = np.mean(schema['value'])
            else:
                row_value = float(row['value'])
            x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), int(300))
            pdf = norm.pdf(x, scale=sigma) * row_value
            S[int(i * 100):int((i + 3) * 100)] += pdf
        if trim:
            S = S[100:-100]
        if vlen:
            return_vector, offset = [], 0
            step = int(len(S) / vlen)
            for i in range(vlen):
                tick = S[offset]
                offset += step
                return_vector.append(tick)
            S = return_vector
        if normed:
            S = (S - np.min(S)) / (np.max(S) - np.min(S))
        return S

    def get_dist(self, sequence, schema, sigma=0.8, vlen=100, trim=False, normalize=False, standardize=False,
                 normed=False, norm_range=(-1, 1)):
        """
        Get distribution of single physiochemical property
        :param sequence: protein sequence
        :param schema: string; pthysicocheical property to model
        :param sigma: sigma used for modeling individual amino acid residues
        :param vlen: return vector length
        :param trim: trim flanking slices of return vector
        :param normalize: normalize values prior to modeling
        :param standardize: standardize values prior to modeling
        :param normed: return vector is normalized to range [0,1]
        :param norm_range: tuple range for normalizing prior to modeling
        :return: 1d array
        """
        schema = get_schema(schema)
        schema = self._prepare_schema(schema, normalize=normalize, standardize=standardize, norm_range=norm_range)
        dist = self._model_dist(sequence, schema, sigma=sigma, vlen=vlen, trim=trim, normed=normed)
        return dist

    @property
    def schemas(self):
        """
        Return list of valid schemas to use, including manually added schemas.
        :return: list
        """
        return list_schema_names()
